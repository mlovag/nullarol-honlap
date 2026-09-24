---
kod: "S3-M3-03"
cim: "Díjak és rejtett költségek — hol szivárog el a pénz"
szemeszter: 3
modul: "Bank, fizetés, digitális biztonság"
modulSorszam: 3
sorszam: 3
hossz: 30
vitaLecke: false
statusz: "megirva"
kulcsuzenet: >-
  A kis, ismétlődő díjak — számladíj, tranzakciós költség, előfizetés, rossz
  árfolyam — egyenként aprónak tűnnek, de évek alatt nagy összeggé adnak össze;
  a védelem az, hogy ismered őket, évente átnézed, és mindig a teljes költséget
  hasonlítod össze, nem a fejlécben szereplő árat.
valosEset: >-
  Magyar tranzakciós illeték (2013 óta): a bankok minden átutalás után
  illetéket fizetnek az államnak, 2024 augusztusa óta 0,45%-ot (tranzakciónként
  max. 20 000 Ft), készpénzfelvételnél 0,9%-ot felső határ nélkül,
  devizakonverziónál 2024 októberétől +0,45% kiegészítő illetéket — ezt
  jellemzően áthárítják az ügyfelekre (adóincidencia). A lakosság havonta két
  készpénzfelvételt 2026. február 1-jétől összesen 300 000 Ft-ig díjmentesen
  intézhet; az azonnali lakossági QR/NFC fizetés illetékmentes.
hetiMegfigyeles: >-
  Kérd meg egy felnőttet, hogy nézzétek át együtt az előző hónap
  bankszámla-kivonatát (az összegeket letakarva, ha szeretné): keressétek meg
  az összes díjat, illetéket és ismétlődő előfizetést. Ha lenne saját számlád
  és előfizetéseid, nézd át a sajátjaidat is: van-e olyan, amit már nem
  használsz?
fogalmak:
  - hu: "Rejtett költség"
    en: "hidden cost / hidden fee"
    mit: >-
      Olyan díj, amely a döntés pillanatában nem látszik (apró betű, szétszórt
      tételek, utolsó lépés) — egyenként kicsi, összeadva nagy.
  - hu: "Tranzakciós illeték"
    en: "financial transaction levy"
    mit: >-
      Magyar állami adó az átutalásokra és készpénzfelvételre, amit a bank
      fizet, de jellemzően áthárít az ügyfeleire.
  - hu: "Dinamikus devizaátváltás (DCC)"
    en: "dynamic currency conversion (DCC)"
    mit: >-
      Amikor külföldön a terminál „forintban” ajánlja a fizetést — általában
      rosszabb árfolyamon; fizess mindig helyi pénznemben.
---

## Horog

Képzeld el, hogy egy vödörben tartod a vizet, és az alján van egy tűhegynyi lyuk. Percenként egy csepp. Ha ránézel, nem látsz semmit. Egy nap múlva a vödör félig üres.

A pénzügyekben ugyanígy működnek a kis, ismétlődő költségek. Egy 3 ezer forintos streaming-előfizetés, amit már alig nézel, évente 36 ezer. Egy „csak” 300 forintos kártyadíj hónapról hónapra. Egy nyaraláson, amikor a terminál megkérdezi: „forintban vagy euróban szeretne fizetni?” és te a forintot választod, mert az ismerősebb — és ezzel észrevétlenül több százalékkal többet fizetsz. Egyenként egyik sem tűnik nagynak. De évek alatt ezek a cseppek adják ki a legtöbb elfolyt pénzt. Ez a lecke megmutatja, hol vannak a lyukak.

## A lecke

**Először: miért kell díjat fizetni — és miért nem látszik?**

Az első leckében láttad, hogy a bank a kamatrésből és díjakból él ([S3-M3-01](/tananyag/mit-csinal-egy-bank/)). A díjak önmagukban nem „rosszak”: a bank dolgozói, az informatika, a biztonság pénzbe kerülnek, és ezt valakinek meg kell fizetnie. A probléma nem a díj léte, hanem az, hogy **nem látod**. Egy termék áránál ott van a szám a polcon. A pénzügyi szolgáltatásoknál a díjak gyakran szétszórtak: egy havi számlavezetési díj, egy kártyadíj, tranzakciónkénti költség, egy külön díj a külföldi készpénzfelvételre. Egyenként kicsik, és csak a számlakivonaton látszanak.

Az 1. modulban láttad, hogy az emberi agy a „szemtől szembe” látható árakra reagál, a rejtett, apró költségekre alig. A **rejtett költség** (*hidden cost*) — az a költség, amely nem jelenik meg a döntés pillanatában, vagy csak az apró betűs részben — ezért hatékonyabb bevételi forrás egy cég számára, mint egy látható áremelés. A dark pattern leckében ([S3-M1-03](/tananyag/marketing-a-fejedben/)) már láttad ennek egy változatát: a fizetés utolsó lépésében megjelenő „kezelési díjat”.

**Másodszor: a leggyakoribb lyukak.**

*Banki díjak és illetékek.* A számlavezetési díj, a kártyadíj, az átutalási díj és a készpénzfelvételi díj bankonként és számlacsomagonként nagyon eltérő. Magyarországon ehhez jön az állami **tranzakciós illeték**, erről a valós esetben részletesen. Egy fiatal, aki havonta néhány utalást csinál és főleg kártyával fizet, egy diák-számlacsomaggal gyakran nagyjából ingyen megoldhatja a bankolást — egy rosszul választott csomaggal évente tízezreket fizethet.

*Előfizetések.* A zene, a videó, a játékok, a felhőtárhely, az appok — mind havidíjas. Mindegyik kicsi, de összeadva egy fiatal felnőttnél könnyen havi tízezres tétel lesz. A trükk itt az **alapértelmezett beállítás** ([S3-M1-02](/tananyag/a-jelen-es-a-jovo-ened/)): az előfizetés magától megy tovább, lemondani kell aktívan. Az „ingyenes próbaidőszak” is erre épül: a cég abban bízik, hogy elfelejted lemondani.

*Devizaváltás.* Külföldön vagy külföldi webshopban fizetve a pénzedet át kell váltani (emlékszel az árfolyamra, [S2-M5-02](/tananyag/az-arfolyam/)?). Ha a terminál vagy a webshop felajánlja, hogy „forintban” fizess, az a **dinamikus devizaátváltás** (*dynamic currency conversion, DCC*): ilyenkor nem a bankod, hanem a kereskedő partnere vált, általában jóval rosszabb árfolyamon. Az ökölszabály: **mindig a helyi pénznemben fizess**, és hagyd, hogy a saját bankod váltson.

*Befektetési díjak.* Ez még előtted van, de érdemes most megjegyezni: a befektetési alapok és biztosítások éves díja — ami „csak” 1–2 százaléknak tűnik — évtizedek alatt a hozam jelentős részét elviheti. Az 5. modulban látni fogod, miért.

**Harmadszor: hogyan tapaszd be a lyukakat?**

Az első szabály: **mindig a teljes költséget hasonlítsd össze**, ne a fejlécben szereplő árat. Egy „ingyenes” számla, amelynél minden utalásért fizetsz, drágább lehet, mint egy havidíjas, amelyben benne vannak az utalások. Ezért vannak kötelező, egységes mutatók: a hiteleknél a **THM** (a 4. modulban, [S3-M4-02](/tananyag/a-kamat-es-a-thm/)), a befektetéseknél a teljes költség mutató, a bankszámláknál pedig az MNB és a bankok összehasonlító oldalai. Ezeket azért találták ki, hogy a szétszórt díjakat egyetlen számmá alakítsák.

A második: **évente egyszer nézd át**. Érdemes egy napot kijelölni (például a születésnapod után), amikor átnézed a számlakivonatot, az előfizetéseket és a banki csomagot: mit használsz tényleg, miért fizetsz feleslegesen, van-e jobb ajánlat? Egy óra munka évi tízezreket spórolhat.

A harmadik: **értsd meg, ki fizeti a végén**. A második szemeszterben tanultál az **adóincidenciáról** ([S2-M4-02](/tananyag/adok/)): nem az fizeti az adót, akire kivetik, hanem akire át lehet hárítani. A pénzügyi díjaknál is így van: amit egy bankra vagy kereskedőre kivetnek, az gyakran a te díjaidban vagy az árakban köt ki.

## Valós eset

**A magyar tranzakciós illeték — egy adó, amit a bank fizet, de te érzel.** Magyarországon 2013 óta létezik a pénzügyi tranzakciós illeték: a bankok és pénzügyi szolgáltatók minden átutalás, készpénzfelvétel és bizonyos más tranzakciók után illetéket fizetnek az államnak. Az illeték mértéke azóta többször emelkedett; 2024 augusztusa óta átutalásoknál 0,45 százalék (tranzakciónként legfeljebb 20 ezer forint), készpénzfelvételnél 0,9 százalék felső határ nélkül, és 2024 októberétől a devizaátváltásos tranzakciókra egy további 0,45 százalékos kiegészítő illeték is vonatkozik.

A törvény szerint az illetéket a bank fizeti — a gyakorlatban viszont a bankok jellemzően áthárítják az ügyfeleikre, tranzakciós díjak formájában. Ez az adóincidencia tankönyvi példája. A lakossági ügyfeleket néhány szabály védi: a törvény szerint havonta két készpénzfelvétel díjmentes, 2026. február 1-jétől összesen 300 ezer forintig, és a magánszemélyek által indított azonnali, QR-kódos vagy érintéses fizetések (a qvik, [S3-M3-02](/tananyag/szamla-kartya-azonnali-fizetes/)) mentesek az illeték alól. Aki ismeri ezeket a szabályokat, az tízezreket spórolhat évente — aki nem, az csendben fizeti. A konkrét mértékek és határok az évek során változnak; a mintázat — az apró, szétszórt, áthárított költség — marad. *(Források: [RSM Hungary — Pénzügyi tranzakciós illeték kisokos](https://www.rsm.hu/kisokos/penzugyi-tranzakcios-illetek); [Biztos Döntés — Így változik a bankszámlahasználat 2026-ban](https://biztosdontes.hu/cikkek/igy-valtozik-a-bankszamlahasznalat-2026-ban).)*

## Döntési dilemma

Két számlacsomag közül választasz az egyetemi éveidre:

1. **„Ingyenes” számla:** nincs havidíj, de minden hagyományos átutalás után 200 forintot plusz az illetéket fizetsz, a kártya éves díja 3000 forint, és külföldön minden készpénzfelvétel 3 százalék.
2. **Havidíjas diákcsomag:** havi 800 forint, de benne van korlátlan utalás, a kártya, és a külföldi kártyás fizetés is kedvezményes.

Melyik a jobb? Nem kell számolnod — gondold végig inkább: mit csinálsz egy tipikus hónapban (hány utalás, utazol-e külföldre, mennyit fizetsz QR-kóddal)? Melyik szokásodra melyik csomag „épült”? És miért nevezi az egyiket a bank „ingyenesnek”?

## Beszélgetésindítók

1. Hány előfizetése van a családodnak (zene, videó, játék, app)? Tudod-e mindegyikről, mennyibe kerül és mennyit használjátok?
2. Miért jó egy cégnek, ha a díjai kicsik és szétszórtak, ahelyett hogy egyetlen árat mondana? Hogyan védekezhet ez ellen a vásárló?
3. Igazságos-e szerinted a tranzakciós illeték? Ki fizeti valójában — és milyen viselkedést ösztönöz (például a készpénz vagy a qvik használatát)?

## Heti megfigyelés

Kérd meg egy felnőttet, hogy nézzétek át együtt az előző hónap bankszámla-kivonatát (az összegeket letakarva, ha szeretné): keressétek meg az összes díjat, illetéket és ismétlődő előfizetést. Ha lenne saját számlád és előfizetéseid, nézd át a sajátjaidat is: van-e olyan, amit már nem használsz?

## Összefoglaló

A pénzügyi szolgáltatásoknak ára van, és ez rendben van — a gond az, hogy a díjak gyakran rejtettek, szétszórtak és kicsik, ezért nem vesszük észre őket. A leggyakoribb lyukak: banki díjak és illetékek, a magától megújuló előfizetések, a rossz árfolyamú devizaátváltás (fizess mindig helyi pénznemben), és később a befektetési díjak. A védelem három szabály: a teljes költséget hasonlítsd össze, ne a fejlécárat; évente egyszer nézd át a díjaidat és előfizetéseidet; és értsd meg, hogy amit a bankra vagy a kereskedőre vetnek ki, azt gyakran te fizeted — ahogy a magyar tranzakciós illeték mutatja. A rejtett költségeknél azonban van egy sokkal veszélyesebb fenyegetés: amikor valaki nem apránként, hanem egyszerre, szándékos megtévesztéssel akarja elvinni a pénzedet. A következő lecke a csalásokról és az adathalászatról szól — és a „túl szép ajánlat” anatómiájáról.
