from main import *

listaPrzedmiotow = []
iloscPrzedmiotow = -1
objetoscPlecaka = -1

b = '0'
while b != '1' and b != '2':
    print("     Wybierz metodę wprowadzenia danych:")
    print("     - 1 - Wprowadź z klawiatury")
    print("     - 2 - Wprowadź z pliku")
    b = input('--> ')

# WPROWADZANIE DANYCH OD UZYTKOWNIKA
if b == '1':
    while True:
        try:
            print('Podaj (liczbę przedmiotów) (objętość plecaka)')
            s = list(map(int, input().split()))
        except ValueError:
            continue
        if len(s) == 2 and s[0] >= 0 and s[1] >= 0:
            break
    iloscPrzedmiotow = s[0]
    objetoscPlecaka = s[1]
    dane_wprowadzone_przez_uzytkownika = []
    dane_wprowadzone_przez_uzytkownika.append(s)
    for i in range(dane_wprowadzone_przez_uzytkownika[0][0]):
        while True:
            try:
                print('Podaj (rozmiar) (wartosc)')
                s = list(map(int, input( str(i) + ":").split()))
            except ValueError:
                continue
            if len(s) == 2 and s[0] >= 0 and s[1] >= 0:
                break
        dane_wprowadzone_przez_uzytkownika.append(s)
    iloscPrzedmiotow, objetoscPlecaka, listaPrzedmiotow = stworzListePrzedmiotowKlawiatura(dane_wprowadzone_przez_uzytkownika)

# WPROWADZ DANE Z PLIKU
if b == '2':
    iloscPrzedmiotow, objetoscPlecaka, listaPrzedmiotow = stworzListePrzedmiotowPliku('inpu.txt')

if listaPrzedmiotow != None:
    print("----------------------------------------------")
    print("Ilość przedmiotów:", iloscPrzedmiotow)
    print("Objętość plecaka:", objetoscPlecaka)
    print("Przedmioty:")
    for i in listaPrzedmiotow:
        i.WypiszPrzedmiot()
    print("----------------------------------------------")

while True:
    if listaPrzedmiotow == None:
        print("Błąd przy pobieraniu danych.")
        break
    a = '0'
    while a != '1' and a != '2' and a != '3' and a != '4':
        print()
        print("Wybierz algorytm do rozwiązania problemu plecakowego:")
        print("- 1 - Algorytm Programowania Dynamicznego (APD)")
        print("- 2 - Algorytm Zachłanny (AZ)")
        print("- 3 - Algorytm Wyczerpujący (AW)")
        print("- 4 - Wyjscie z programu")
        a = input('--> ')
        print()
    if a == '4':
        print("Wyjście")
        break
    elif a == '1':
        AlgorytmProgramowaniaDynamicznego(listaPrzedmiotow, objetoscPlecaka)
    elif a == '2':
        AlgorytmZachlanny(listaPrzedmiotow, objetoscPlecaka)
    elif a == '3':
        AlgorytmWyczerpujacy(listaPrzedmiotow, objetoscPlecaka)


