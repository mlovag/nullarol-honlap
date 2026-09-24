---
kod: "S3-M3-05"
cim: "Kripto — mi ez valójában, és mi nem"
szemeszter: 3
modul: "Bank, fizetés, digitális biztonság"
modulSorszam: 3
sorszam: 5
hossz: 30
vitaLecke: true
statusz: "megirva"
kulcsuzenet: >-
  A kripto egy valódi technológiai újdonság (központi szereplő nélküli digitális
  tulajdon), de nem betét, nincs mögötte bevétel vagy állami garancia, ára
  rendkívül ingadozik, és a csalók kedvenc terepe — hogy mire jó, arról komoly
  szakértők is ellentétesen gondolkodnak, de aki hozzányúl, annak értenie kell,
  mit vesz és mit kockáztat.
valosEset: >-
  FTX, 2022. november: a világ egyik legnagyobb kriptotőzsdéje napok alatt
  összeomlott, mert az ügyfelek pénzét titokban a tulajdonos kapcsolt cége
  használta; Sam Bankman-Friedet 2024 márciusában 25 év börtönre ítélték.
  Ellenpélda: 2024 januárjában az amerikai SEC engedélyezte a
  bitcoin-ETF-eket, nagy vagyonkezelők léptek be. Magyarország: 2025 júliusi
  szigorú szabályozás (validálási kötelezettség, büntetőjogi szankciók) — több
  szolgáltató, köztük a Revolut felfüggesztette magyar kriptoszolgáltatásait;
  2026-ban az új kormány visszavonta a korlátozásokat.
hetiMegfigyeles: >-
  Kövesd egy héten át a bitcoin árát (bármely híroldal árfolyam-oldalán), és
  hasonlítsd össze az euró–forint árfolyam mozgásával. Mennyivel mozgott
  többet? Keress egy kriptos reklámot vagy posztot, és nézd meg: megtalálod
  benne a csalások négy jelét (S3-M3-04)?
fogalmak:
  - hu: "Kriptoeszköz"
    en: "crypto-asset (cryptocurrency)"
    mit: >-
      Digitális érték, amelyet nem bank vagy állam, hanem egy közös, nyilvános
      főkönyv tart nyilván; nem betét, nem részvény, nincs mögötte bevétel vagy
      garancia.
  - hu: "Blokklánc"
    en: "blockchain"
    mit: >-
      Sok számítógépen közösen vezetett, titkosítással védett nyilvános
      főkönyv, amelyet utólag gyakorlatilag lehetetlen meghamisítani.
  - hu: "Volatilitás"
    en: "volatility"
    mit: >-
      Mennyire és milyen gyorsan ingadozik egy eszköz ára — minél nagyobb,
      annál kevésbé kiszámítható, mennyit ér holnap.
  - hu: "Stabilcoin"
    en: "stablecoin"
    mit: >-
      Olyan kriptoeszköz, amelynek értékét egy hagyományos pénzhez (többnyire
      a dollárhoz) kötik, és a kibocsátó elvileg tartalékot tart mögötte.
---

## Horog

Egy floridai programozó, Laszlo Hanyecz 2010. május 22-én egy internetes fórumon felajánlotta, hogy 10 000 bitcoint fizet két pizzáért. Valaki elfogadta. A két pizza akkor nagyjából 40 dollárba került. A 10 000 bitcoin értéke a 2020-as évek közepén több száz millió dollár volt — a történelem legdrágább pizzája. A kriptorajongók máig minden évben ünneplik ezt a napot.

Egy másik történet: 2022 novemberében az FTX, a világ egyik legnagyobb kriptotőzsdéje, amelynek reklámjaiban világhíres sportolók szerepeltek, napok alatt összeomlott. Ügyfelek milliói nem fértek hozzá a pénzükhöz. Az alapítóját később 25 év börtönre ítélték csalásért.

Melyik történet mondja el az igazságot a kriptóról? Valószínűleg mindkettő — és egyik sem egyedül. Ez a lecke egy **vita-lecke**: elmondja, mi a kripto tényszerűen, majd mindkét oldal legjobb érveit bemutatja, forrással. A döntés a tiéd.

## A lecke

**Először: mi a kripto — tényszerűen?**

A **kriptoeszköz** (*crypto-asset*, köznyelvben kriptopénz) olyan digitális érték, amelynek a nyilvántartását nem egy bank vagy állam vezeti, hanem sok számítógép közösen, egy **blokkláncnak** (*blockchain*) nevezett nyilvános főkönyvben. Gondolj rá úgy, mint egy közös, a világ sok pontján tárolt füzetre, amelybe minden tranzakciót beírnak, és amelyet a titkosítás (kriptográfia — innen a név) miatt gyakorlatilag lehetetlen utólag meghamisítani. Az első és legismertebb a **bitcoin**, amelyet 2009-ben indított el egy máig ismeretlen személy vagy csoport „Satoshi Nakamoto” néven. A bitcoin mennyisége a szabályai szerint legfeljebb 21 millió lehet.

Fontos, hogy mi *nem* a kripto. A második szemeszterben láttad, mitől pénz a pénz: a forintot az MNB bocsátja ki, az állam elfogadja adófizetésre, és a jegybank célja az értékének megőrzése ([S2-M2-01](/tananyag/honnan-jon-a-penz/), [S2-M2-04](/tananyag/az-mnb-es-az-inflacios-cel/)). A kriptó mögött nincs jegybank, nincs állami garancia. Nem **betét**: az OBA nem védi ([S3-M3-01](/tananyag/mit-csinal-egy-bank/)). És nem is **részvény**: egy részvény mögött egy cég áll, amely bevételt és nyereséget termel (erről az 5. modulban), a bitcoin viszont semmilyen bevételt nem termel — az árát kizárólag az határozza meg, hogy mennyit hajlandó valaki fizetni érte. Az ára ezért rendkívül ingadozik: ezt az ingadozást **volatilitásnak** (*volatility*) hívják. A bitcoin ára egy-egy évben többször is feleződött vagy duplázódott.

A kriptoeszközök között vannak **stabilcoinok** (*stablecoins*) is, amelyek értékét egy hagyományos pénzhez, többnyire a dollárhoz kötik, és amelyek mögött a kibocsátó (elvileg) tényleges dollártartalékot tart. Az EU-ban 2024 óta a MiCA-rendelet szabályozza a kriptoszolgáltatókat.

**Másodszor: az érvek a kripto mellett.**

*1. Központi szereplő nélküli, cenzúraálló tulajdon.* A támogatók szerint a bitcoin legnagyobb újdonsága, hogy két ember közvetítő — bank, állam — nélkül cserélhet értéket az interneten, és senki nem tudja befagyasztani vagy elkobozni. Ez olyan országokban lehet különösen fontos, ahol a helyi pénz nagyon gyorsan veszti az értékét (emlékszel a hiperinflációra és a bizalomra?), vagy ahol a kormány korlátozza a pénzmozgást.

*2. Korlátozott kínálat — „digitális arany”.* Mivel a bitcoin mennyisége nem növelhető 21 millió fölé, a támogatók szerint hosszú távon az aranyhoz hasonló értékmegőrző lehet — szélsőségesen szűkös (emlékszel: a **szűkösség** az ár egyik alapja). Az elfogadás is nőtt: 2024 januárjában az amerikai tőkepiaci felügyelet (SEC) engedélyezte a bitcoinba fektető tőzsdei alapokat, és a világ legnagyobb vagyonkezelői is kínálnak ilyen terméket. A támogatók szerint a blokklánc-technológia (például a stabilcoinok gyors, olcsó nemzetközi átutalásai) a pénzügyi rendszer jövőjének része lehet.

**Harmadszor: az érvek a kripto ellen.**

*1. Nincs mögötte értékteremtés — és rossz pénz.* A kritikusok, köztük az Európai Központi Bank szakértői és híres befektetők, szerint a bitcoin nem termel semmit: nincs bevétele, osztaléka, kamata, az ára csak arra épül, hogy valaki később többet fizet érte. Az EKB szakértői egy 2022-es blogbejegyzésben azt írták, hogy a bitcoin fizetőeszközként sosem vált be, és befektetésként sem indokolt. A szélsőséges volatilitás miatt pénzként is rosszul működik: ki fogadna el fizetésként olyat, ami egy hónap alatt negyedét veszti az értékéből?

*2. Csalások, feltörések, védelem hiánya.* A kriptovilágban nincs betétbiztosítás, az átutalás visszavonhatatlan, és ha elveszted a jelszavadat (a privát kulcsot), a pénzed örökre elveszett. A kriptotőzsdék többször összeomlottak vagy feltörték őket, és az előző leckében látott befektetési csalások és Ponzi-sémák jelentős része kriptóra épül. Ehhez jön a nagy energiafelhasználás és a **szabályozási kockázat**: egy állam egyik napról a másikra megnehezítheti a használatát — ahogy a valós esetben látod.

*Ahol a két oldal egyetért:* a kripto a legkockázatosabb eszközök közé tartozik. Ha valaki befektet bele, csak olyan pénzt tegyen, amelynek az elvesztését elviseli, soha ne a vésztartalékát ([S3-M2-03](/tananyag/vesztartalek/)), és legyen gyanús minden „biztos” kriptohozamra ([S3-M3-04](/tananyag/csalas-es-adathalaszat/)).

## Valós eset

**Az FTX összeomlása — és a magyar kriptohullámvölgy.** Az FTX 2019-ben indult, és néhány év alatt a világ egyik legnagyobb kriptotőzsdéje lett; alapítója, Sam Bankman-Fried a kriptovilág sztárja volt. 2022 novemberében kiderült, hogy az ügyfelek betétjeit titokban a tulajdonos kapcsolt befektetési cége használta kockázatos ügyletekre. Amikor ez napvilágra került, az ügyfelek tömegesen próbálták kivenni a pénzüket — egy bankroham ([S3-M3-01](/tananyag/mit-csinal-egy-bank/)), csak betétbiztosítás és jegybank nélkül. A tőzsde néhány nap alatt csődbe ment, Bankman-Friedet 2024 márciusában egy New York-i bíróság 25 év börtönre ítélte csalásért.

Magyarországon a kriptó szabályozási kockázata közvetlenül látszott. 2025 júliusától egy szigorú törvény előírta, hogy a kripto forintra váltásához egy engedélyezett „validátor” igazolása kell, és az igazolás nélküli váltást büntetőjogi szankciókkal, nagyobb összegeknél több év börtönnel fenyegette. Mivel ilyen validátor gyakorlatilag nem volt, több szolgáltató, köztük a Revolut is felfüggesztette magyarországi kriptoszolgáltatásait, és az EU is vizsgálatot indított. A 2026-os kormányváltás után az új kormány bejelentette, hogy visszavonja a korlátozásokat, és az uniós szabályokhoz igazítja a hazai rendszert. Néhány hónap alatt a magyar kriptohasználók kétszer is újratervezhették a pénzügyeiket — a szabályozási kockázat nem elmélet. *(Források: [U.S. Department of Justice — Samuel Bankman-Fried sentenced to 25 years](https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes); [SEC — Gensler statement on spot bitcoin ETPs, 2024. január 10.](https://www.sec.gov/news/statement/gensler-statement-spot-bitcoin-011023); [ECB blog, 2022. november 30. — Bitcoin’s last stand](https://www.ecb.europa.eu/press/blog/date/2022/html/ecb.blog221130~5de5e4bbf8.en.html); [Cryptofalka, 2026. június 12. — Fordulat a magyar kriptoszabályozásban](https://cryptofalka.hu/kereskedes/fordulat-jon-magyar-kriptos-szabalyozasban-eu-vizsgalat-utan).)*

## Döntési dilemma

18 éves vagy, és van 300 ezer forint megtakarításod (a vésztartalékod külön megvan). Egy barátod a kriptóval „tavaly megduplázta” a pénzét, és rábeszélne. Három lehetőség:

1. **Az egészet kriptóba teszed**, mert a barátodnak bejött, és fiatal vagy, van időd kivárni.
2. **Egy kis részét (például 20–30 ezret) szabályozott, EU-s engedéllyel rendelkező szolgáltatónál kipróbálod** — annyit, amennyi elvesztését nyugodtan elviselnéd —, hogy megértsd, hogyan működik.
3. **Egyáltalán nem nyúlsz hozzá**, amíg nem érted jobban a befektetéseket (az 5. modul után).

Melyiket választod? Melyik 1. modulbeli torzítás hat rád a barátod történeténél (társas bizonyíték, FOMO)? És te hallasz-e a barátoktól arról is, aki a kriptón veszített?

## Beszélgetésindítók

1. Melyik oldal érvei győztek meg jobban — és miért? Van-e olyan érv, ami a másik oldalon is elgondolkodtatott?
2. Mi a különbség egy részvény, egy bankbetét és egy bitcoin között abban, hogy „mi áll mögötte”?
3. Miért vonzó a kripto a csalóknak? Mi az, ami a kriptovilágban hiányzik a banki védelemhez képest?

## Heti megfigyelés

Kövesd egy héten át a bitcoin árát (bármely híroldal árfolyam-oldalán), és hasonlítsd össze az euró–forint árfolyam mozgásával. Mennyivel mozgott többet? Keress egy kriptos reklámot vagy posztot, és nézd meg: megtalálod benne a csalások négy jelét ([S3-M3-04](/tananyag/csalas-es-adathalaszat/))?

## Összefoglaló

A kriptoeszköz digitális érték, amelynek nyilvántartását nem bank vagy állam, hanem egy közös, nyilvános főkönyv, a blokklánc vezeti; a legismertebb a 2009 óta létező, legfeljebb 21 millió darabos bitcoin. Nem betét (az OBA nem védi), nem részvény (nem termel bevételt), és ára rendkívül volatilis. A támogatók szerint központi szereplő nélküli, cenzúraálló, korlátozott kínálatú „digitális arany”, amelyet már nagy intézmények is elfogadnak. A kritikusok szerint nincs mögötte értékteremtés, pénzként rosszul működik, és a csalások, feltörések és szabályozási fordulatok miatt rendkívül kockázatos — ahogy az FTX összeomlása és a magyar kriptoszabályozás hullámvölgye is mutatta. Ezzel lezárul a bankról, fizetésről és biztonságról szóló modul. A következő modul egy olyan eszközről szól, amivel szinte mindenki találkozik az életében, és ami egyszerre lehet a legnagyobb segítség és a legnagyobb csapda: a hitelről.
