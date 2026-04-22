import tkinter as tk
from tkinter import font
import math


class KettaTelefon:

    def __init__(self):
        # Ketta konstandid
        self.KETTA_RAADIUS = 120
        self.KESK_X = 200
        self.KESK_Y = 200
        self.NUMBRID = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.NUMBRITE_NURGAD = [i * 30 for i in range(10)]

        # Pastellvärvide palett
        self.BEEBIROOSA = '#FFB6C1'
        self.PASTELL_ROOSA = '#FFC0CB'
        self.PASTELL_LAVENDEL = '#E6E6FA'
        self.PASTELL_VIRDIK = '#98FB98'
        self.PASTELL_SININE = '#87CEEB'
        self.PASTELL_KREEM = '#FFF5EE'
        self.PASTELL_ORANŽ = '#FFDAB9'
        self.PASTELL_LILLA = '#DDA0DD'
        self.TUME_ROOSA = '#FF69B4'
        self.VALGE = '#FFFFFF'
        self.HELEHALL = '#F0F0F0'

        # Olekumuutujad
        self.olek = "IDLE"
        self.nurk = 0
        self.hiire_algnurk = 0
        self.algne_hiire_nurk = 0
        self.valitud_numbreid = []
        self.tagasi_id = None
        self.animatsiooni_samm = 0

        # Graafiline liides
        self.aken = tk.Tk()
        self.aken.title("Ketastelefon")
        self.aken.geometry("600x650")
        self.aken.configure(bg=self.BEEBIROOSA)
        self.aken.minsize(550, 600)

        # Canvas ketta joonistamiseks
        self.canvas = tk.Canvas(
            self.aken,
            width=420,
            height=420,
            bg=self.PASTELL_KREEM,
            highlightthickness=2,
            highlightbackground=self.PASTELL_ROOSA
        )
        self.canvas.place(x=90, y=30)

        # Valitud numbrite ala
        self.numbrilaud = tk.Frame(
            self.aken,
            bg=self.PASTELL_LAVENDEL,
            relief=tk.RAISED,
            bd=3
        )
        self.numbrilaud.place(x=100, y=480, width=400, height=70)

        self.numbrilabel = tk.Label(
            self.numbrilaud,
            text="Valitud numbrid",
            font=('Comic Sans MS', 12, 'bold'),
            bg=self.PASTELL_LAVENDEL,
            fg='#8B008B'
        )
        self.numbrilabel.pack(pady=5)

        self.valitud_tekst = tk.StringVar()
        self.valitud_tekst.set("")
        self.valitud_kuvaja = tk.Label(
            self.numbrilaud,
            textvariable=self.valitud_tekst,
            font=('Comic Sans MS', 16, 'bold'),
            bg=self.PASTELL_LAVENDEL,
            fg=self.TUME_ROOSA
        )
        self.valitud_kuvaja.pack()

        # Nupud
        nupuraam = tk.Frame(self.aken, bg=self.BEEBIROOSA)
        nupuraam.place(x=150, y=570, width=300, height=50)

        # Helista nupp - pastellroheline
        self.helista_nupp = tk.Button(
            nupuraam,
            text="HELISTA",
            font=('Comic Sans MS', 12, 'bold'),
            bg=self.PASTELL_VIRDIK,
            fg='#006400',
            activebackground='#90EE90',
            activeforeground='#006400',
            command=self.helista,
            width=12,
            height=1,
            relief=tk.RAISED,
            bd=3
        )
        self.helista_nupp.pack(side=tk.LEFT, padx=10)


        self.uus_nupp = tk.Button(
            nupuraam,
            text="🔄 UUS",
            font=('Comic Sans MS', 12, 'bold'),
            bg=self.PASTELL_ORANŽ,
            fg='#8B4513',
            activebackground='#FFDAB9',
            activeforeground='#8B4513',
            command=self.lahtesta,
            width=8,
            height=1,
            relief=tk.RAISED,
            bd=3
        )
        self.uus_nupp.pack(side=tk.LEFT, padx=10)

        # Kustuta nupp - pastellsinine
        self.kustuta_nupp = tk.Button(
            nupuraam,
            text="KUSTUTA",
            font=('Comic Sans MS', 12, 'bold'),
            bg=self.PASTELL_SININE,
            fg='#00008B',
            activebackground='#87CEEB',
            activeforeground='#00008B',
            command=self.kustuta_viimane,
            width=10,
            height=1,
            relief=tk.RAISED,
            bd=3
        )
        self.kustuta_nupp.pack(side=tk.LEFT, padx=10)

        # Animatsiooni ala
        self.animatsiooni_tekst = tk.StringVar()
        self.animatsiooni_label = tk.Label(
            self.aken,
            textvariable=self.animatsiooni_tekst,
            font=('Comic Sans MS', 16, 'bold'),
            bg=self.BEEBIROOSA,
            fg=self.TUME_ROOSA
        )

        # Abitekst
        self.abitekst = tk.Label(
            self.aken,
            text="Hoia hiirt all ja keera ketast päripäeva\nVabasta number valimiseks",
            font=('Comic Sans MS', 9),
            bg=self.BEEBIROOSA,
            fg='#8B008B',
            wraplength=500
        )
        self.abitekst.place(x=50, y=625)

        # Dekoratiivsed südamed
        self.dekoratsioonid()

        # Hiire sündmused
        self.canvas.bind("<Button-1>", self.hiire_vajutus)
        self.canvas.bind("<B1-Motion>", self.hiire_liigutus)
        self.canvas.bind("<ButtonRelease-1>", self.hiire_vabastus)

        # Joonista ketas
        self.joonista_ketas()

    def dekoratsioonid(self):
        """Lisa dekoratiivsed elemendid"""
        # Südamed akna ülaossa
        südamed = ["💖", "🌸", "💕", "🌷", "💗"]
        for i, süda in enumerate(südamed):
            label = tk.Label(
                self.aken,
                text=süda,
                font=('Arial', 16),
                bg=self.BEEBIROOSA
            )
            label.place(x=20 + i * 50, y=5)

        # Alumisse serva ka
        for i, süda in enumerate(südamed):
            label = tk.Label(
                self.aken,
                text=süda,
                font=('Arial', 16),
                bg=self.BEEBIROOSA
            )
            label.place(x=20 + i * 50, y=620)

    def joonista_ketas(self):
        self.canvas.delete("all")

        # Varjuefekt (helehall)
        self.canvas.create_oval(
            self.KESK_X - self.KETTA_RAADIUS + 3,
            self.KESK_Y - self.KETTA_RAADIUS + 3,
            self.KESK_X + self.KETTA_RAADIUS + 3,
            self.KESK_Y + self.KETTA_RAADIUS + 3,
            outline='',
            fill='#E0E0E0',
            width=0
        )

        # Ketta välimine ring
        self.canvas.create_oval(
            self.KESK_X - self.KETTA_RAADIUS,
            self.KESK_Y - self.KETTA_RAADIUS,
            self.KESK_X + self.KETTA_RAADIUS,
            self.KESK_Y + self.KETTA_RAADIUS,
            outline=self.TUME_ROOSA,
            width=3,
            fill=self.PASTELL_ROOSA
        )

        # Ketta sisemine ring
        self.canvas.create_oval(
            self.KESK_X - 25,
            self.KESK_Y - 25,
            self.KESK_X + 25,
            self.KESK_Y + 25,
            outline=self.TUME_ROOSA,
            width=2,
            fill=self.VALGE
        )

        # Keskel süda
        self.canvas.create_text(
            self.KESK_X,
            self.KESK_Y,
            text="💖",
            font=('Arial', 24),
            fill=self.TUME_ROOSA
        )

        # Märk ketta peal
        märgi_nurk = math.radians(self.nurk)
        märgi_x = self.KESK_X + 35 * math.sin(märgi_nurk)
        märgi_y = self.KESK_Y - 35 * math.cos(märgi_nurk)
        self.canvas.create_oval(
            märgi_x - 5,
            märgi_y - 5,
            märgi_x + 5,
            märgi_y + 5,
            fill=self.TUME_ROOSA,
            outline='#FF1493',
            width=2
        )

        # Numbrid pastellvärvides
        pastell_numbrid = [
            self.PASTELL_LILLA, self.PASTELL_SININE, self.PASTELL_VIRDIK,
            self.PASTELL_ORANŽ, self.PASTELL_ROOSA, self.PASTELL_LAVENDEL,
            self.PASTELL_KREEM, self.PASTELL_LILLA, self.PASTELL_SININE,
            self.PASTELL_VIRDIK
        ]

        for i, number in enumerate(self.NUMBRID):
            nurk = math.radians(self.NUMBRITE_NURGAD[i])
            x = self.KESK_X + (self.KETTA_RAADIUS - 25) * math.sin(nurk)
            y = self.KESK_Y - (self.KETTA_RAADIUS - 25) * math.cos(nurk)

            # Iga numbri taust
            self.canvas.create_oval(
                x - 12,
                y - 12,
                x + 12,
                y + 12,
                fill=pastell_numbrid[i],
                outline=self.TUME_ROOSA,
                width=2
            )

            # Number
            self.canvas.create_text(
                x, y,
                text=number,
                font=('Comic Sans MS', 16, 'bold'),
                fill='#8B008B'
            )

            # Väike dekoratiivne täpp iga numbri juures
            punkt_x = self.KESK_X + (self.KETTA_RAADIUS - 12) * math.sin(nurk)
            punkt_y = self.KESK_Y - (self.KETTA_RAADIUS - 12) * math.cos(nurk)
            self.canvas.create_oval(
                punkt_x - 2,
                punkt_y - 2,
                punkt_x + 2,
                punkt_y + 2,
                fill=self.TUME_ROOSA
            )

    def arvuta_nurk_hiirest(self, x, y):
        """Arvuta hiire asukohast nurk"""
        dx = x - self.KESK_X
        dy = y - self.KESK_Y
        nurk = math.degrees(math.atan2(dx, -dy))
        if nurk < 0:
            nurk += 360
        return nurk

    def hiire_vajutus(self, event):
        """Hiire vajutus"""
        if self.olek not in ["IDLE", "CALLING"]:
            return

        kaugus = math.sqrt((event.x - self.KESK_X) ** 2 + (event.y - self.KESK_Y) ** 2)
        if kaugus <= self.KETTA_RAADIUS:
            self.olek = "DIALLING"
            self.hiire_algnurk = self.arvuta_nurk_hiirest(event.x, event.y)
            self.algne_hiire_nurk = self.nurk

    def hiire_liigutus(self, event):
        """Hiire liigutus"""
        if self.olek != "DIALLING":
            return

        uus_nurk = self.arvuta_nurk_hiirest(event.x, event.y)
        nurk_vahe = uus_nurk - self.hiire_algnurk

        if nurk_vahe < 0:
            nurk_vahe += 360

        uus_ketta_nurk = self.algne_hiire_nurk + nurk_vahe
        if uus_ketta_nurk <= 330:
            self.nurk = uus_ketta_nurk
            self.joonista_ketas()

    def hiire_vabastus(self, event):
        """Hiire vabastus"""
        if self.olek != "DIALLING":
            return

        number = self.leia_lähim_number()
        if number is not None and len(self.valitud_numbreid) < 10:
            self.valitud_numbreid.append(number)
            self.uuenda_numbreid()
            self.näita_teadet(f"Valisid numbri {number}!")
        elif number is None:
            self.näita_teadet("Proovi uuesti!")

        self.olek = "RETURNING"
        self.liigu_tagasi()

    def leia_lähim_number(self):
        """Leia lähim number"""
        if self.nurk < 0 or self.nurk > 330:
            return None

        lahim_nurk = min(self.NUMBRITE_NURGAD, key=lambda x: abs(x - self.nurk))
        if abs(lahim_nurk - self.nurk) <= 15:
            indeks = self.NUMBRITE_NURGAD.index(lahim_nurk)
            return self.NUMBRID[indeks]
        return None

    def liigu_tagasi(self):
        """Animeeri tagasiliikumine"""
        if self.olek != "RETURNING":
            return

        if self.nurk > 0:
            self.nurk -= 4
            self.joonista_ketas()
            self.tagasi_id = self.aken.after(20, self.liigu_tagasi)
        else:
            self.nurk = 0
            self.joonista_ketas()
            self.olek = "IDLE"
            self.tagasi_id = None

    def uuenda_numbreid(self):
        """Uuenda numbrite kuvamist"""
        tekst = " ".join(self.valitud_numbreid)
        self.valitud_tekst.set(tekst)

    def kustuta_viimane(self):
        """Kustuta viimane number"""
        if self.valitud_numbreid and self.olek != "CALLING":
            self.valitud_numbreid.pop()
            self.uuenda_numbreid()
            self.näita_teadet("Viimane number kustutatud!")

    def helista(self):
        """Helista"""
        if self.olek == "CALLING":
            self.näita_teadet("Helistan")
            return

        if len(self.valitud_numbreid) == 0:
            self.näita_teadet("Palun vali number enne helistamist")
            return

        if self.tagasi_id:
            self.aken.after_cancel(self.tagasi_id)

        self.olek = "CALLING"
        self.helistamise_animatsioon(0)

    def helistamise_animatsioon(self, samm):
        """Helistamise animatsioon"""
        self.animatsiooni_samm = samm

        if samm == 0:
            self.animatsiooni_tekst.set("HELISTAN")
            self.animatsiooni_label.place(x=200, y=250)
        elif samm == 4:
            self.animatsiooni_tekst.set("HELISTAN.")
        elif samm == 8:
            self.animatsiooni_tekst.set("HELISTAN..")
        elif samm == 12:
            self.animatsiooni_tekst.set("HELISTAN...")
        elif samm == 16:
            number = "".join(self.valitud_numbreid)
            self.animatsiooni_tekst.set(f"Helistasin numbrile {number}")
            self.aken.after(2000, lambda: self.animatsiooni_label.place_forget())
            self.olek = "IDLE"
            return

        self.aken.after(150, lambda: self.helistamise_animatsioon(samm + 1))

    def näita_teadet(self, teade):
        """Kuva ajutine teade"""
        self.animatsiooni_tekst.set(teade)
        self.animatsiooni_label.place(x=180, y=250)
        self.aken.after(2000, lambda: self.animatsiooni_label.place_forget())

    def lahtesta(self):
        """Lähtesta süsteem"""
        if self.tagasi_id:
            self.aken.after_cancel(self.tagasi_id)

        self.olek = "IDLE"
        self.nurk = 0
        self.valitud_numbreid = []
        self.animatsiooni_samm = 0

        self.valitud_tekst.set("")
        self.animatsiooni_label.place_forget()
        self.joonista_ketas()
        self.näita_teadet("Süsteem lähtestatud!")

    def käivita(self):
        """Käivita rakendus"""
        self.aken.mainloop()


if __name__ == "__main__":
    telefon = KettaTelefon()
    telefon.käivita()