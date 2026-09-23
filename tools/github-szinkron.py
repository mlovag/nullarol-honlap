#!/usr/bin/env python3
"""
Nulláról honlap — szinkron a helyi mappa és a GitHub tároló között.

Git nélkül működik, a GitHub API-n keresztül (így a mappában nem kell
semmit törölni). A kulcsot a mappa gyökerében lévő `.github-token` fájlból
olvassa, és azt soha nem tölti fel.

Használat (a Honlap mappából):
  python3 tools/github-szinkron.py allapot      # mi tér el, merre
  python3 tools/github-szinkron.py le           # GitHub -> helyi (csak a GitHubon változott fájlok)
  python3 tools/github-szinkron.py fel "üzenet" # helyi -> GitHub, egy commitban
  python3 tools/github-szinkron.py alap         # a mostani állapot legyen a közös kiindulópont
  python3 tools/github-szinkron.py alap-github  # a GitHub mostani állapota a kiindulópont
                                                 # (minden helyi eltérés = helyi módosítás)

Háromutas összevetés: helyi / GitHub / a legutóbbi közös állapot
(.szinkron-allapot.json). Ha egy fájl mindkét oldalon változott,
ütközésként jelzi, és nem ír felül semmit.
"""
import hashlib, json, os, sys, base64, fnmatch, urllib.request, urllib.error

REPO = "mlovag/nullarol-honlap"
AG = "main"
GYOKER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN_FAJL = os.path.join(GYOKER, ".github-token")
ALLAPOT_FAJL = os.path.join(GYOKER, ".szinkron-allapot.json")
KIHAGY = ["node_modules", "dist", ".astro", ".git", "_to_delete", ".github-token", ".github-token.txt",
          ".szinkron-allapot.json", ".DS_Store", "*.log", ".env", ".vercel",
          "__pycache__", "desktop.ini", "Thumbs.db", "~$*"]

def kihagyando(ut):
    return any(fnmatch.fnmatch(r, m) for r in ut.split("/") for m in KIHAGY)

def token(kotelezo=True):
    global TOKEN_FAJL
    if not os.path.exists(TOKEN_FAJL) and os.path.exists(TOKEN_FAJL + ".txt"):
        TOKEN_FAJL += ".txt"   # a Jegyzettömb néha .txt-t tesz a végére
    if not os.path.exists(TOKEN_FAJL):
        if kotelezo:
            sys.exit("Nincs .github-token fájl a Honlap mappában.")
        return None
    return open(TOKEN_FAJL, encoding="utf-8-sig").read().strip()

def api(modszer, ut, adat=None):
    fejlec = {"Accept": "application/vnd.github+json",
              "X-GitHub-Api-Version": "2022-11-28",
              "User-Agent": "nullarol-szinkron"}
    t = token(kotelezo=(modszer != "GET"))   # olvasáshoz (publikus tároló) nem kell kulcs
    if t:
        fejlec["Authorization"] = "Bearer " + t
    req = urllib.request.Request(
        "https://api.github.com" + ut, method=modszer,
        data=json.dumps(adat).encode() if adat is not None else None,
        headers=fejlec)
    try:
        with urllib.request.urlopen(req, timeout=60) as v:
            return json.loads(v.read() or b"null")
    except urllib.error.HTTPError as e:
        sys.exit(f"GitHub hiba {e.code} ({modszer} {ut}): {e.read().decode()[:400]}")

def blob_sha(tartalom):
    return hashlib.sha1(b"blob %d\0" % len(tartalom) + tartalom).hexdigest()

def helyi():
    f = {}
    for gy, mappak, fajlok in os.walk(GYOKER):
        rel = os.path.relpath(gy, GYOKER).replace(os.sep, "/")
        mappak[:] = [m for m in mappak if not kihagyando((rel + "/" + m).lstrip("./"))]
        for n in fajlok:
            ut = (n if rel == "." else rel + "/" + n)
            if not kihagyando(ut):
                f[ut] = blob_sha(open(os.path.join(GYOKER, ut), "rb").read())
    return f

def tavoli():
    ref = api("GET", f"/repos/{REPO}/git/ref/heads/{AG}")
    commit = ref["object"]["sha"]
    c = api("GET", f"/repos/{REPO}/git/commits/{commit}")
    fa = api("GET", f"/repos/{REPO}/git/trees/{c['tree']['sha']}?recursive=1")
    return commit, c["tree"]["sha"], {e["path"]: e["sha"] for e in fa["tree"] if e["type"] == "blob"}

def alap_betolt():
    if os.path.exists(ALLAPOT_FAJL):
        return json.load(open(ALLAPOT_FAJL, encoding="utf-8"))
    return None

def alap_ment(commit, fajlok):
    json.dump({"commit": commit, "fajlok": fajlok}, open(ALLAPOT_FAJL, "w", encoding="utf-8"), indent=1)

def osszevet():
    H = helyi(); commit, fa, T = tavoli(); A = alap_betolt()
    if A is None:
        sys.exit("Nincs közös kiindulópont (.szinkron-allapot.json). Először: alap")
    B = A["fajlok"]
    helyben, tavol, utkozes = [], [], []
    for ut in sorted(set(H) | set(T) | set(B)):
        h, t, b = H.get(ut), T.get(ut), B.get(ut)
        if h == t: continue
        if t == b: helyben.append(ut)       # csak helyben változott (vagy új)
        elif h == b: tavol.append(ut)       # csak a GitHubon változott
        else: utkozes.append(ut)
    return H, T, commit, fa, helyben, tavol, utkozes

def kiir(cim, lista):
    if lista:
        print(cim); [print("   ", u) for u in lista]

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    p = sys.argv[1]
    if p == "alap-github":
        commit, _, T = tavoli(); alap_ment(commit, T)
        print(f"Kiindulópont = GitHub {commit[:7]}, {len(T)} fájl."); return
    if p == "alap":
        commit, _, T = tavoli(); H = helyi()
        kozos = {u: s for u, s in T.items() if H.get(u) == s}
        alap_ment(commit, kozos)
        print(f"Kiindulópont rögzítve ({commit[:7]}), {len(kozos)} közös fájl.")
        return
    H, T, commit, fa, helyben, tavol, utk = osszevet()
    if p == "allapot":
        kiir("Helyben változott (feltöltendő):", helyben)
        kiir("A GitHubon változott (letöltendő):", tavol)
        kiir("ÜTKÖZÉS (mindkét helyen változott):", utk)
        if not (helyben or tavol or utk): print("Minden szinkronban.")
    elif p == "le":
        for ut in tavol:
            if ut in T:
                b = api("GET", f"/repos/{REPO}/git/blobs/{T[ut]}")
                cel = os.path.join(GYOKER, *ut.split("/"))
                os.makedirs(os.path.dirname(cel), exist_ok=True)
                open(cel, "wb").write(base64.b64decode(b["content"]))
                print("letöltve:", ut)
            else:
                print("a GitHubon törölve (helyben megmarad, kézzel töröld):", ut)
        B = alap_betolt()["fajlok"]
        for ut in tavol:
            if ut in T: B[ut] = T[ut]
            else: B.pop(ut, None)
        alap_ment(commit, B)
        kiir("ÜTKÖZÉS — ezekhez nem nyúltam:", utk)
    elif p == "fel":
        if utk:
            kiir("ÜTKÖZÉS — előbb ezeket kell rendezni, nem töltöttem fel semmit:", utk); sys.exit(1)
        uzenet = sys.argv[2] if len(sys.argv) > 2 else "Frissítés"
        fel = [u for u in helyben if u in H]
        torolt = [u for u in helyben if u not in H]
        if not fel and not torolt:
            print("Nincs mit feltölteni."); return
        elemek = []
        for ut in fel:
            tart = open(os.path.join(GYOKER, *ut.split("/")), "rb").read()
            b = api("POST", f"/repos/{REPO}/git/blobs",
                    {"content": base64.b64encode(tart).decode(), "encoding": "base64"})
            elemek.append({"path": ut, "mode": "100644", "type": "blob", "sha": b["sha"]})
        for ut in torolt:
            elemek.append({"path": ut, "mode": "100644", "type": "blob", "sha": None})
        uj_fa = api("POST", f"/repos/{REPO}/git/trees", {"base_tree": fa, "tree": elemek})
        uj = api("POST", f"/repos/{REPO}/git/commits",
                 {"message": uzenet, "tree": uj_fa["sha"], "parents": [commit]})
        api("PATCH", f"/repos/{REPO}/git/refs/heads/{AG}", {"sha": uj["sha"], "force": False})
        B = alap_betolt()["fajlok"]
        for ut in fel: B[ut] = H[ut]
        for ut in torolt: B.pop(ut, None)
        alap_ment(uj["sha"], B)
        print(f"Feltöltve: {uj['sha'][:7]} — {uzenet}")
        for u in fel: print("   +", u)
        for u in torolt: print("   -", u)
    else:
        sys.exit(__doc__)

if __name__ == "__main__":
    main()
