from abc import ABC, abstractmethod
import random
import time


# baasklass - mängus osalejad pärinevad siit
class Tegelane(ABC):

    def __init__(self, nimi, elud):
        # kaitstud väljad - otse ei muudeta
        self.nimi = nimi
        self._elu = elud
        self._max_elu = elud

    # loeme elusid ilma otse muutmata
    @property
    def elu(self):
        return self._elu

    # kahju vastuvõtmine - ei lähe alla nulli
    def võta_kahju(self, punktid):
        self._elu = max(0, self._elu - punktid)
        print(f"{self.nimi} kaotab {punktid} elu. Elud: {self._elu}/{self._max_elu}")

    # elusoleku kontroll
    def on_elus(self):
        return self._elu > 0

    # iga tegelane ründab isemoodi
    @abstractmethod
    def ründa(self, kes):
        pass

    def __str__(self):
        return f"{self.nimi} ({self._elu}/{self._max_elu})"


# Sõdalane - tugev, aga lihtne
class Sõdalane(Tegelane):

    def __init__(self, nimi, elud):
        super().__init__(nimi, elud)
        self._soomus = random.randint(1, 5)  # natuke soomust

    # sõdalane lihtsalt lööb
    def ründa(self, kes):
        if not self.on_elus():
            print(f"{self.nimi} on liiga väsinud...")
            return

        kahju = random.randint(10, 20)
        print(f"\n{self.nimi} (sõdalane) lajub mõõgaga!")
        kes.võta_kahju(kahju)


# Maag - vajab manat
class Maag(Tegelane):

    def __init__(self, nimi, elud, manat=50):
        super().__init__(nimi, elud)
        self._mana = manat
        self._max_mana = manat

    # loeme manat
    @property
    def mana(self):
        return self._mana

    # maag kulutab manat
    def ründa(self, kes):
        if not self.on_elus():
            print(f"{self.nimi} ei saa rünnata...")
            return

        if self._mana < 10:
            print(f"\n{self.nimi} (maag) üritab loitsida, aga mana on otsas!")
            return

        self._mana -= 10
        kahju = random.randint(15, 25)
        print(f"\n{self.nimi} (maag) loitsib! (mana: {self._mana}/{self._max_mana})")
        kes.võta_kahju(kahju)


# Vibukütt - kasutab nooli
class Vibukütt(Tegelane):

    def __init__(self, nimi, elud, nooli=30):
        super().__init__(nimi, elud)
        self._nooled = nooli
        self._osavus = random.uniform(0.7, 0.95)  # tabamise tõenäosus

    @property
    def nooled(self):
        return self._nooled

    # vibukütt laseb vibust
    def ründa(self, kes):
        if not self.on_elus():
            print(f"{self.nimi} on liiga nõrk...")
            return

        if self._nooled < 1:
            print(f"\n{self.nimi} (vibukütt) üritab lasta, aga nooli pole!")
            return

        self._nooled -= 1

        # kas tabab?
        if random.random() < self._osavus:
            kahju = random.randint(8, 18)
            print(f"\n{self.nimi} (vibukütt) laseb noole! (alles: {self._nooled})")
            kes.võta_kahju(kahju)
        else:
            print(f"\n{self.nimi} (vibukütt) laseb mööda...")


# Paladin - püha sõdalane, saab ravida
class Paladin(Tegelane):

    def __init__(self, nimi, elud, pühadus=60):
        super().__init__(nimi, elud)
        self._pühadus = pühadus
        self._loendur = 0

    @property
    def pühadus(self):
        return self._pühadus

    # ravib ennast kui vaja
    def _ravi(self):
        if self._pühadus < 8:
            return

        ravib = random.randint(5, 15)
        self._pühadus -= 4
        self._elu = min(self._max_elu, self._elu + ravib)
        print(f"{self.nimi} palvetab ja ravib +{ravib} (pühadus: {self._pühadus})")

    # paladin ründab või ravib
    def ründa(self, kes):
        if not self.on_elus():
            return

        self._loendur += 1

        # iga kolmas kord ravib kui vaja
        if self._loendur % 3 == 0 and self._elu < self._max_elu * 0.6:
            self._ravi()
            return

        if self._pühadus < 5:
            print(f"\n{self.nimi} (paladin) on liiga nõrk...")
            return

        self._pühadus -= 2
        kahju = random.randint(6, 16) + int(self._pühadus * 0.15)
        print(f"\n{self.nimi} (paladin) ründab püha jõuga! (pühadus: {self._pühadus})")
        kes.võta_kahju(kahju)


#lahingufunktsioon - töötab kõigiga
def lahing(t1, t2):
    print("\n" + "=" * 50)
    print(f"{t1.nimi} VS {t2.nimi}")
    print("=" * 50)

    ring = 1
    while t1.on_elus() and t2.on_elus():
        print(f"\n--- ring {ring} ---")

        t1.ründa(t2)
        if not t2.on_elus():
            print(f"\n{t2.nimi} langes!")
            break

        t2.ründa(t1)
        if not t1.on_elus():
            print(f"\n{t1.nimi} langes!")
            break

        time.sleep(0.8)
        ring += 1

    print("\n" + "=" * 50)
    if t1.on_elus():
        print(f"VOITIS: {t1.nimi}")
    else:
        print(f"VOITIS: {t2.nimi}")
    print("=" * 50)


# käivitame testimise
if __name__ == "__main__":

    # kontrollime, kas abstraktset klassi saab luua
    try:
        test = Tegelane("test", 100)
        print("see ei tohiks töötada")
    except TypeError:
        print("õige - abstraktset klassi ei saa luua")

    print("\n" + "MANG ALGAB".center(50))
    print("-" * 50)

    # loome tegelased
    s = Sõdalane("Ragnar", 120)
    m = Maag("Zed", 80, 55)
    v = Vibukütt("Lark", 90, 12)
    p = Paladin("Uther", 100, 45)

    # näitame kes on
    for tegelane in [s, m, v, p]:
        print(f"-> {tegelane}")

    # esimene lahing
    print("\n" + "LAHING 1".center(50))
    lahing(s, v)

    # teine lahing
    print("\n" + "LAHING 2".center(50))
    lahing(m, p)

    # näitame, et väljad on kaitstud
    print("\n" + "KONTROLL".center(50))
    print(f"maag: mana = {m.mana}")
    print(f"vibukütt: nooli = {v.nooled}")
    print(f"paladin: pühadus = {p.pühadus}")
    print("(valjastpoolt otse muuta ei saa)")

    print("\n" + "LOPP".center(50))