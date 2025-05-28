using System;
using System.Collections.Generic;

class Ksiazka
{
    public int id_k;
    public string tytul;
    public string autor;
    public bool dostepnosc_k = true;
}

class Uzytkownik
{
    public string imie;
    public string nazwisko;
    public int id_u;
}

class Wypozyczania
{
    public Ksiazka w_ksiazka;
    public Uzytkownik w_uzytkownik;
}

class Biblioteka
{
    public List<Ksiazka> ksiazki = new List<Ksiazka>();
    public List<Uzytkownik> uzytkownicy = new List<Uzytkownik>();
    public List<Wypozyczania> wypozyczenia = new List<Wypozyczania>();
    private int nastepneID_uzytkownika = 1;

    public void dodaj_ksiazke(int id_k, string tytul, string autor)
    {
        Ksiazka ksiazka = new Ksiazka() { id_k = id_k, tytul = tytul, autor = autor };
        ksiazki.Add(ksiazka);
    }

    public int dodaj_uzytkownika(string imie, string nazwisko)
    {
        Uzytkownik uzytkownik = new Uzytkownik()
        {
            imie = imie,
            nazwisko = nazwisko,
            id_u = nastepneID_uzytkownika++
        };
        uzytkownicy.Add(uzytkownik);
        Console.WriteLine($"Zostales dodany do systemu twoje imie:{uzytkownik.imie} twoje nazwisko: {uzytkownik.nazwisko} twoje ID: {uzytkownik.id_u}");
        return uzytkownik.id_u;
    }

    public void wypozycz_ksiazke(int id_ksiazki, int id_u)
    {
        Ksiazka ksiazka = ksiazki.Find(k => k.id_k == id_ksiazki && k.dostepnosc_k);
        Uzytkownik uzytkownik = uzytkownicy.Find(u => u.id_u == id_u);

        if (ksiazka != null && uzytkownik != null)
        {
            Wypozyczania nowe = new Wypozyczania()
            {
                w_ksiazka = ksiazka,
                w_uzytkownik = uzytkownik
            };
            wypozyczenia.Add(nowe);
            ksiazka.dostepnosc_k = false;

            Console.WriteLine($"wybrales tytul {ksiazka.tytul} twoje imie:{uzytkownik.imie} twoje nazwisko; {uzytkownik.nazwisko}.");
        }
        else
        {
            Console.WriteLine("Brak ksiazki w systemie");
        }
    }

    public void pokaz_dostepne_ksiazki()
    {
        Console.WriteLine("\n Ksiazki znajdujace sie w bibliotece:");
        foreach (var ksiazka in ksiazki)
        {
            if (ksiazka.dostepnosc_k)
                Console.WriteLine($"ID: {ksiazka.id_k} -{ksiazka.tytul} ----{ksiazka.autor}");
        }
    }
}

class Program
{
    static void Main()
    {
        Biblioteka moja_biblioteka = new Biblioteka();

        moja_biblioteka.dodaj_ksiazke(1, "Krzyzacy", "Henryk Sienkiewicz");
        moja_biblioteka.dodaj_ksiazke(2, "Lalka", "Bolesław Prus");
        moja_biblioteka.dodaj_ksiazke(3, "Pan Tadeusz", "Adam Mickiewicz");
        moja_biblioteka.dodaj_ksiazke(4,"W pustyni i w puszczy", "Henryk Sienkiewicz");
        moja_biblioteka.dodaj_ksiazke(5,"Zbrodnia i kara", "Fiodor Dostojewski");
        moja_biblioteka.dodaj_ksiazke(6,"1984", "George Orwell");
        moja_biblioteka.dodaj_ksiazke(7,"Dziady", "Adam Mickiewicz");

        Console.Write("Podaj swoje imie: ");
        string imie = Console.ReadLine();

        Console.Write("Podaj swoje nazwisko: ");
        string nazwisko = Console.ReadLine();

        int id_u = moja_biblioteka.dodaj_uzytkownika(imie, nazwisko);

        moja_biblioteka.pokaz_dostepne_ksiazki();

        Console.Write("Wybierz ksiazke - podaj ID: ");
        int id_ksiazki = int.Parse(Console.ReadLine());

        moja_biblioteka.wypozycz_ksiazke(id_ksiazki, id_u);
    }
}
