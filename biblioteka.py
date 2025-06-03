class Ksiazka:
    def d_ksiazki(self, id_k, tytul, autor):
        self.id_k = id_k
        self.tytul = tytul
        self.autor = autor
        self.dostepnosc_k = True

class Uzytkownik:
    def d_uzytkownik(self, imie, nazwisko, id_u):
        self.imie = imie
        self.nazwisko = nazwisko
        self.id_u = id_u

class Wypozyczanie:
    def d_wypozyczenie(self, ksiazka, uzytkownik):
        self.w_ksiazka = ksiazka
        self.w_uzytkownik = uzytkownik

class Biblioteka:
    def d_B(self):
        self.ksiazki = []
        self.uzytkownicy = []
        self.wypozyczenia = []
        self.nastepne_id_uzytkownika = 1

    def dodaj_ksiazke(self, id_k, tytul, autor):
        ksiazka = Ksiazka()
        ksiazka.d_ksiazki(id_k, tytul, autor)
        self.ksiazki.append(ksiazka)

    def dodaj_uzytkownika(self, imie, nazwisko):
        uzytkownik = Uzytkownik()
        uzytkownik.d_uzytkownik(imie, nazwisko, self.nastepne_id_uzytkownika)
        self.nastepne_id_uzytkownika += 1
        self.uzytkownicy.append(uzytkownik)
        print(f"Dodano do systemu-Imię: {uzytkownik.imie}, -Nazwisko: {uzytkownik.nazwisko}, -ID: {uzytkownik.id_u}")
        return uzytkownik.id_u

    def wypozycz_ksiazke(self, id_ksiazki, id_u):
        ksiazka = next((k for k in self.ksiazki if k.id_k == id_ksiazki and k.dostepnosc_k), None)
        uzytkownik = next((u for u in self.uzytkownicy if u.id_u == id_u), None)

        if ksiazka and uzytkownik:
            wypozyczenie = Wypozyczanie()
            wypozyczenie.d_wypozyczenie(ksiazka, uzytkownik)
            self.wypozyczenia.append(wypozyczenie)
            ksiazka.dostepnosc_k = False
            print(f"posiadana książka: {ksiazka.tytul}, Imię: {uzytkownik.imie}, Nazwisko: {uzytkownik.nazwisko}.")
        

    def zwroc_ksiazke(self, id_ksiazki, id_u):
        wypozyczenie = next((w for w in self.wypozyczenia if w.w_ksiazka.id_k == id_ksiazki and w.w_uzytkownik.id_u == id_u), None)
        if wypozyczenie:
            wypozyczenie.w_ksiazka.dostepnosc_k = True
            self.wypozyczenia.remove(wypozyczenie)
            print(f"książka zostala zwrócona")
        else:
            print("Podałes złe ID książki.")

    def pokaz_dostepne_ksiazki(self):
        print("\nKsiążki dostępne w bibliotece:")
        for ksiazka in self.ksiazki:
            if ksiazka.dostepnosc_k:
                print(f"ID: {ksiazka.id_k} - {ksiazka.tytul} --- {ksiazka.autor}")

biblioteka = Biblioteka()
biblioteka.d_B()

biblioteka.dodaj_ksiazke(1, "Krzyżacy", "Henryk Sienkiewicz")
biblioteka.dodaj_ksiazke(2, "Lalka", "Bolesław Prus")
biblioteka.dodaj_ksiazke(3, "Pan Tadeusz", "Adam Mickiewicz")
biblioteka.dodaj_ksiazke(4, "W pustyni i w puszczy", "Henryk Sienkiewicz")
biblioteka.dodaj_ksiazke(5, "Zbrodnia i kara", "Fiodor Dostojewski")
biblioteka.dodaj_ksiazke(6, "1984", "George Orwell")
biblioteka.dodaj_ksiazke(7, "Dziady", "Adam Mickiewicz")

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
id_u = biblioteka.dodaj_uzytkownika(imie, nazwisko)

biblioteka.pokaz_dostepne_ksiazki()

id_ksiazki = int(input("Wybierz książkę-podaj ID: "))
biblioteka.wypozycz_ksiazke(id_ksiazki, id_u)
id_ksiazki_zwrot = int(input("Wybierz książkę którą chcesz zwrocic-podaj ID: "))
biblioteka.zwroc_ksiazke(id_ksiazki_zwrot, id_u)
