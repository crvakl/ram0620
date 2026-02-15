def int_to_roman(arv):
    if arv < 1 or arv > 1000: #Kontrollime, et sisestatud arv oleks 1-1000 vahemikus
        return "Arv peab olema vahemikus 1 kuni 1000"

    vaartused = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    sumbol = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman = ""

    for i in range(len(vaartused)): #Käime kõik väärtused läbi, ning lahutame nii palju kui on võimalik
        while arv >= vaartused[i]:
            roman += sumbol[i]    #lisame sümboli
            arv -= vaartused[i]
    return roman                  #tagastame saadud rooma arvu

def main():
    while True:  #tekkitame lõpmatu sisendi küsimist, kuni kasutaja ei vajuta "stop"
        sisend = input("Sisesta arv (1-1000) või 'stop' lõpetamiseks: ").strip()

        if sisend.lower() == "stop":
            print("Programm lõpetas töö!")
            break

        try:   #püüame vigu
            arv = int(sisend)
            tulemus = int_to_roman(arv)
            print(tulemus)
        except ValueError:
            print("Viga: Palun sisesta täisarv!")

if __name__ == "__main__":
    main()
