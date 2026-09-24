---
kod: "S3-M3-01"
cim: "Mit csinál valójában egy bank? — a pénzed a bankban"
szemeszter: 3
modul: "Bank, fizetés, digitális biztonság"
modulSorszam: 3
sorszam: 1
hossz: 30
vitaLecke: false
statusz: "megirva"
kulcsuzenet: >-
  A bank nem széf, hanem közvetítő: a betétedet hitelként továbbadja, és a két
  kamat különbségéből él — ezért működik bizalomra, ezért lehet bankroham, és
  ezért fontos tudnod, hogy a betétedet a betétbiztosítás (Magyarországon az
  OBA) meddig védi.
valosEset: >-
  Silicon Valley Bank, 2023. március: a bank a betétek nagy részét hosszú
  lejáratú kötvényekbe tette, amelyek a kamatemelések miatt értéket vesztettek;
  amikor ez kiderült, a betétesek egyetlen nap alatt (március 9.) kb. 42
  milliárd dollárt próbáltak kivenni, másnap a hatóságok bezárták — a betétek
  túl nagy része nem volt biztosítva. Magyar példa: 2022 március, Sberbank
  Magyarország — az MNB visszavonta az engedélyét, az OBA kifizette a
  betéteseket. OBA-védelem: személyenként és bankonként 100 ezer euróig.
hetiMegfigyeles: >-
  Nézd meg egy-két magyar bank honlapján: mennyi kamatot adnak egy éves
  lekötött betétre, és mennyi a személyi kölcsön vagy lakáshitel kamata (THM)?
  Mekkora a különbség? Keresd meg a bank oldalán az OBA-logót vagy a
  betétbiztosítási tájékoztatót is.
fogalmak:
  - hu: "Betét"
    en: "deposit"
    mit: >-
      A bankban tartott pénzed — a bank nem fiókban őrzi, hanem nagy részét
      hitelként továbbadja, ezért fizet rá kamatot.
  - hu: "Kamatrés"
    en: "interest rate spread (net interest margin)"
    mit: >-
      A hitelekre kért és a betétekre fizetett kamat különbsége — ebből él a
      bank.
  - hu: "Lejárati transzformáció"
    en: "maturity transformation"
    mit: >-
      A bank bármikor kivehető betétekből hosszú távú hiteleket csinál —
      hasznos, de sebezhetővé teszi, ha mindenki egyszerre kéri vissza a
      pénzét.
  - hu: "Bankroham"
    en: "bank run"
    mit: >-
      Amikor a betétesek egyszerre akarják kivenni a pénzüket, mert félnek,
      hogy a bank bajban van — önbeteljesítő jóslat.
  - hu: "Betétbiztosítás (OBA)"
    en: "deposit insurance"
    mit: >-
      Ha egy bank csődbe megy, az Országos Betétbiztosítási Alap személyenként
      és bankonként 100 ezer euróig kifizeti a betéteket — befektetést és
      kriptót nem véd.
---

## Horog

A legtöbb ember úgy képzeli el a bankot, mint egy nagy széfet: beteszed a pénzed, ott ül a nevével egy fiókban, és amikor kell, kiveszed. Ha ez igaz lenne, a bank nem tudna neked kamatot fizetni — sőt, neked kellene fizetned a megőrzésért, ahogy egy csomagmegőrzőért is fizetsz. Mégis a bank ad neked kamatot. Honnan veszi?

Egy csütörtökön, 2023. március 9-én, az Egyesült Államok 16. legnagyobb bankjának, a Silicon Valley Banknak az ügyfelei egyetlen nap alatt nagyjából 42 milliárd dollárt próbáltak kivenni a számláikról — főleg telefonról, néhány óra alatt. Másnap délelőtt a hatóságok bezárták a bankot. A pénz nem volt ott. Nem mert ellopták, hanem mert a bank pontosan azt csinálta vele, amit minden bank csinál. Ez a lecke erről szól.

## A lecke

**Először: a bank közvetítő, nem széf.**

A második szemeszterben megismerted a **kereskedelmi bankot** és a pénzteremtést ([S2-M2-01](/tananyag/honnan-jon-a-penz/)) — akkor a gazdaság szemszögéből. Most nézzük meg a saját szemeddel. Amikor pénzt teszel a számládra, azt **betétnek** (*deposit*) hívják. A bank ezt a pénzt nem teszi félre egy fiókba: nagy részét **hitelként** továbbadja — egy családnak lakásvásárlásra, egy cégnek egy új gépre —, vagy állampapírba, kötvénybe fekteti. A bank tehát **közvetítő** (*financial intermediary*): összeköti azokat, akiknek éppen fölösleges pénzük van, azokkal, akiknek éppen szükségük van rá.

A bank a hitelekért magasabb kamatot kér, mint amit a betétekért fizet. Ha a betétedre évi 3 százalékot kapsz, egy személyi kölcsönért valaki ugyanannak a banknak 10–15 százalékot is fizethet. A kettő közötti különbség a **kamatrés** (*interest rate spread*) — ebből fizeti a bank a dolgozóit, a fiókjait, az informatikát, fedezi azokat a hiteleket, amelyeket nem fizetnek vissza, és ebből van a nyeresége. A bankok emellett díjakból is élnek — számlavezetés, kártya, átutalás —, erről a modul harmadik leckéje szól.

**Másodszor: a bank beépített csapdája — lejárat és bizalom.**

A bank üzletének van egy beépített feszültsége. A betétedet te bármikor kiveheted — ma, holnap, most azonnal a telefonodról. A lakáshitel viszont, amit a bank ugyanebből a pénzből adott, 20 év alatt tér vissza. A bank tehát rövid távú pénzből (betétek) hosszú távú kölcsönt csinál. Ezt **lejárati transzformációnak** (*maturity transformation*) hívják, és ez a bankok egyik legfontosabb hasznos szerepe: nélkülük szinte senki nem tudna lakást venni. Csakhogy ez akkor működik, ha a betétesek nem akarják *egyszerre* kivenni a pénzüket.

Normális esetben nem akarják: mindig van, aki betesz, és van, aki kivesz, és ez kiegyenlítődik. A bank ezért csak a betétek kis részét tartja azonnal elérhető formában. De ha a betétesek elkezdenek félni, hogy a bank bajban van, és mindenki egyszerre akarja kivenni a pénzét, akkor a bank — még ha egészséges is lenne — nem tud mindenkinek azonnal fizetni. Ez a **bankroham** (*bank run*). A bankroham magát beteljesítő jóslat: ha elég sokan hiszik, hogy a bank csődbe megy, akkor csődbe is megy. A bank tehát szinte szó szerint **bizalomra** épül — ez a tananyag egyik visszatérő alapfogalma.

**Harmadszor: mi védi a pénzedet?**

A történelem sok bankrohamot látott, ezért az államok három védővonalat építettek ki. Az első a **szabályozás és felügyelet**: a bankoknak előírt mértékű saját tőkével és likvid tartalékkal kell rendelkezniük, és ezt Magyarországon az MNB felügyeli. A második a **jegybank mint végső hitelező**: válságban a jegybank kölcsönözhet a bajba jutott, de alapvetően egészséges bankoknak.

A harmadik — és a te szempontodból a legfontosabb — a **betétbiztosítás** (*deposit insurance*). Magyarországon ezt az **Országos Betétbiztosítási Alap (OBA)** végzi: ha egy bank csődbe megy, az OBA a betéteseknek személyenként és bankonként legfeljebb **100 ezer eurónak** megfelelő összeget kifizet (ez az EU-ban mindenhol így van). Ennek két fontos következménye van. Az egyik: a legtöbb ember betétje teljes egészében biztonságban van, ezért nincs oka pánikba esni — és ezért ritka a bankroham. A másik: a védelem **nem terjed ki mindenre**. A 100 ezer euró fölötti rész, a részvények, a befektetési alapok és például a kriptoeszközök nem betétek, így az OBA nem védi őket (a befektetésekre külön szabályok vonatkoznak, erről az 5. modulban). Aki egy nem banknál, hanem egy „szuper hozamot” ígérő cégnél tartja a pénzét, annak semmilyen betétbiztosítása nincs — ez a csalásokról szóló leckében ([S3-M3-04](/tananyag/csalas-es-adathalaszat/)) fontos lesz.

## Valós eset

**A Silicon Valley Bank összeomlása, 2023.** A kaliforniai Silicon Valley Bank (SVB) a technológiai startupok bankja volt. A 2020–21-es években, amikor a startupok rengeteg befektetői pénzt kaptak, a betétei gyorsan megnőttek. A bank ennek a pénznek nagy részét hosszú lejáratú amerikai állampapírokba és jelzáloghoz kötött kötvényekbe fektette — alacsony, de biztosnak tűnő kamattal. Amikor 2022-ben az amerikai jegybank gyorsan emelni kezdte a kamatot az infláció miatt (ahogy az MNB is, [S2-M2-05](/tananyag/a-kamat/)), ezeknek a kötvényeknek az ára jelentősen esett — hiszen ki venne meg egy alacsony kamatú régi kötvényt, ha újat magasabb kamattal is vehet? A lejárati transzformáció csapdája becsapódott.

A bank 2023. március 8-án bejelentette, hogy veszteséggel adott el kötvényeket, és tőkét próbál bevonni. A hír a startupos közösségben perceken belül terjedt a közösségi médiában és chatcsoportokban, és március 9-én a betétesek nagyjából 42 milliárd dollárt próbáltak kivenni — a történelem egyik leggyorsabb bankrohamát. A betétek szokatlanul nagy része nem volt biztosítva, mert a cégeknek jóval több pénzük volt a banknál, mint a biztosított határ — így volt okuk pánikba esni. Március 10-én a hatóságok bezárták a bankot. A tovaterjedést megelőzendő az amerikai kormány végül rendkívüli döntéssel minden betétest kártalanított.

Magyarországon is volt rá példa, hogy a betétbiztosításnak működnie kellett: 2022 márciusában, az orosz–ukrán háború kitörése után, az orosz hátterű Sberbank magyar leányvállalata a szankciók miatt fizetésképtelenné vált, az MNB visszavonta az engedélyét, és az OBA kifizette a betéteseket a biztosított határig. *(Források: [FDIC — Lessons Learned from the U.S. Regional Bank Failures of 2023](https://www.fdic.gov/news/speeches/2024/lessons-learned-us-regional-bank-failures-2023); [Fortune, 2023. március 11. — $42 billion attempted withdrawals in one day](https://fortune.com/2023/03/11/silicon-valley-bank-run-42-billion-attempted-withdrawals-in-one-day); [Federal Reserve OIG — Material Loss Review of Silicon Valley Bank](https://oig.federalreserve.gov/reports/board-material-loss-review-silicon-valley-bank-sep2023.pdf).)*

## Döntési dilemma

Képzeld el, hogy 30 éves vagy, és eladtál egy kis vállalkozást: a számládon hirtelen 60 millió forint van (ez több mint 100 ezer euró). A bankod ugyanazt a kamatot adja, mint a többi bank. Három lehetőség:

1. **Minden marad egy bankban** — egyszerű, áttekinthető, és „ez egy nagy, biztos bank”.
2. **Szétosztod több bank között** úgy, hogy egyikben se legyen több, mint a biztosított határ — több számla, több app, több figyelnivaló.
3. **A nagy részét magyar állampapírba teszed**, amely nem betét, hanem az állam tartozik neked közvetlenül, és csak egy kisebb részt tartasz bankszámlán.

Melyiket választod? Mennyire valószínű, hogy egy nagy bank csődbe megy — és mekkora a kár, ha mégis? Mit tanulhatsz az SVB-s cégektől, akik mindent egy helyen tartottak?

## Beszélgetésindítók

1. Miért fizet kamatot a bank a betétedre, ha „csak megőrzi”? Hogyan írnád le egy kisebb testvérnek egy mondatban, mit csinál egy bank?
2. Miért lehet, hogy egy egészséges bank is csődbe megy egy bankroham miatt? Mi a szerepe ebben a közösségi médiának?
3. Igazságos volt-e, hogy az amerikai kormány az SVB minden betétesét kártalanította, azokat is, akiknek több volt a biztosított határnál? Milyen ösztönzőt ad ez a jövőre nézve?

## Heti megfigyelés

Nézd meg egy-két magyar bank honlapján: mennyi kamatot adnak egy éves lekötött betétre, és mennyi a személyi kölcsön vagy lakáshitel kamata (THM)? Mekkora a különbség? Keresd meg a bank oldalán az OBA-logót vagy a betétbiztosítási tájékoztatót is.

## Összefoglaló

A bank nem széf, hanem közvetítő: a betétedet hitelként továbbadja vagy befekteti, és a hitelkamat és a betéti kamat közötti különbségből, a kamatrésből él (plusz a díjakból). Rövid távú betétekből hosszú távú hiteleket csinál — ez a lejárati transzformáció, ami nélkül nem lenne lakáshitel, de ami miatt a bank bizalomra épül: ha mindenki egyszerre akarja kivenni a pénzét, bankroham tör ki, ahogy 2023-ban a Silicon Valley Banknál. A pénzedet a szabályozás, a jegybank és a betétbiztosítás védi: Magyarországon az OBA személyenként és bankonként 100 ezer euróig téríti meg a betéteket — de csak a betéteket, a befektetéseket és a nem banki „ajánlatokat” nem. A következő lecke a bank mindennapi eszközeiről szól: számla, kártya, azonnali fizetés — a magyar rendszer a gyakorlatban.
