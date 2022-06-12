from GrafyPrzejscia import *
from main import *

dane_wprowadzone_przez_uzytkownika = []

b = '0'
while b != '1' and b != '2' and b != '3':
    print("     Wybierz metodę wprowadzenia danych:")
    print("     - 1 - Wprowadź z klawiatury")
    print("     - 2 - Wprowadź z pliku")
    b = input('--> ')

# WPROWADZANIE DANYCH OD UZYTKOWNIKA
if b == '1':
    print('Podaj liczbe wierzcholkow i krawedzi po spacji')
    s = list(map(int, input().split()))
    dane_wprowadzone_przez_uzytkownika = []
    dane_wprowadzone_przez_uzytkownika.append(s)
    print('Podaj wierzcholki parami')
    for i in range(dane_wprowadzone_przez_uzytkownika[0][1]):
        s = list(map(int, input().split()))
        dane_wprowadzone_przez_uzytkownika.append(s)

# SPRAWDZANIE CZY JEST CYKL DLA GRAFU SKIEROWANEGO
czy_jest_cykl = True
def sprawdz_czy_jest_cykl_skierowany():
    global czy_jest_cykl
    czy_jest_cykl = True

    if b == '1':
        czy_jest_cykl = sprawdz_czy_jest_cykl(dane_wprowadzone_przez_uzytkownika)
        if not czy_jest_cykl:
            print()
            print("GRAF WEJŚCIOWY JEST ACYKLICZNY")
            print("WYKONYWANIE PROGRAMU ZOSTAJE PRZERWANE")
            return False
    else:
        ans = []
        file = open('inpu.txt', 'r')
        s = list(map(int, file.readline().split()))
        ans.append(s)
        liczba_krawedzi = s[1]
        for i in range(liczba_krawedzi):
            s = list(map(int, file.readline().split()))
            ans.append(s)
        file.close()
        czy_jest_cykl = sprawdz_czy_jest_cykl(ans)
        if not czy_jest_cykl:
            print()
            print("GRAF WEJŚCIOWY JEST ACYKLICZNY")
            print("WYKONYWANIE PROGRAMU ZOSTAJE PRZERWANE")
            return False
    return True



while True:
    a = '0'
    while a != '1' and a != '2' and a != '3' and a != '4':
        print()
        print("     Wybierz strukture:")
        print("     - 1 - Macierz sasiedztwa")
        print("     - 2 - Lista nastepnikow")
        print("     - 3 - Wyjscie z programu")
        a = input('--> ')
        print()
    if a == '3':
        print('Bye Bye')
        break
    elif b == '1':
        if a == '1':
            # MACIERZ SASIEDZTWA Z KLAWIATURY
            macierz = stworz_macierz_sasiedztwa_nieskierowana_z_klawiatury(dane_wprowadzone_przez_uzytkownika)
            print('-----------------------------')
            print('Struktura macierzy sasiedztwa')
            print('-----------------------------')
            for i in macierz:
                print(i)
            print('-----------------------------')
            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - znajdz cykl Hamiltona")
                print("- 2 - znajdz cykl Eulera")
                c = input()
            if c == '1':
                znajdz_cykl_hamiltona_macierz_sasiedztwa(macierz)
            else:
                znajdz_cykl_eulera_macierz_sasiedztwa(macierz)

        elif a == '2':
            # LISTA NASTEPNIKOW Z KLAWIATURY
            lista_nastepnikow = stworz_liste_nastepnikow(dane_wprowadzone_przez_uzytkownika)
            print('---------------------------')
            print('Struktura listy nastepnikow')
            print('---------------------------')
            for i in range(len(lista_nastepnikow)):
                print(i, ':', lista_nastepnikow[i])
            print('---------------------------')

            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - znajdz cykl Hamiltona")
                print("- 2 - znajdz cykl Eulera")
                c = input()
            if c == '1':
                znajdz_cykl_hamiltona_lista_nastepnikow(lista_nastepnikow.copy())
            else:
                print("LISTA NASTEPNIKOW EULER")

    elif b == '2':
        if a == '1':
            # MACIERZ SASIEDZTWA Z PLIKU
            macierz = stworz_macierz_sasiedztwa_nieskierowana_z_pliku('inpu.txt')
            print('-----------------------------')
            print('Struktura macierzy sasiedztwa')
            print('-----------------------------')
            for i in macierz:
                print(i)
            print('-----------------------------')

            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - znajdz cykl Hamiltona")
                print("- 2 - znajdz cykl Eulera")
                c = input()
            if c == '1':
                znajdz_cykl_hamiltona_macierz_sasiedztwa(macierz)
            else:
                znajdz_cykl_eulera_macierz_sasiedztwa(macierz)

        elif a == '2':
            # LISTA NASTEPNIKOW Z PLIKU
            lista_nastepnikow = stworz_liste_nastepnikow_z_pliku('inpu.txt')
            print('---------------------------')
            print('Struktura listy nastepnikow')
            print('---------------------------')
            for i in range(len(lista_nastepnikow)):
                print(i, ':', lista_nastepnikow[i])
            print('---------------------------')

            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - znajdz cykl Hamiltona")
                print("- 2 - znajdz cykl Eulera")
                c = input()
            if c == '1':
                znajdz_cykl_hamiltona_lista_nastepnikow(lista_nastepnikow.copy())
            else:
                znajdz_cykl_eulera_lista_nastepnikow(lista_nastepnikow)