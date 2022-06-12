import datetime
import random
from main import *

dane_wprowadzone_przez_uzytkownika = []

b = '0'
while b != '1' and b != '2' and b != '3':
    print("     Wybierz metodę wprowadzenia danych:")
    print("     - 1 - Wprowadź z klawiatury")
    print("     - 2 - Wprowadź z pliku")
    b = input('--> ')

# SPRAWDZANIE CZY JEST CYKL
if b == '1':
    print('Podaj liczbe wierzcholkow i krawedzi po spacji')
    s = list(map(int, input().split()))
    dane_wprowadzone_przez_uzytkownika = []
    dane_wprowadzone_przez_uzytkownika.append(s)
    print('Podaj wierzcholki parami')
    for i in range(dane_wprowadzone_przez_uzytkownika[0][1]):
        s = list(map(int, input().split()))
        dane_wprowadzone_przez_uzytkownika.append(s)

    #print(dane_wprowadzone_przez_uzytkownika)

czy_jest_cykl = True
if b == '1':
    czy_jest_cykl = sprawdz_czy_jest_cykl(dane_wprowadzone_przez_uzytkownika)
    if czy_jest_cykl:
        print()
        print("GRAF POSIADA CYKL")
        print("WYKONYWANIE PROGRAMU ZOSTAJE PRZERWANE")
else:
    ans = []
    file = open('inpu.txt', 'r')
    s = list(map(int, file.readline().split()))
    ans.append(s)
    liczba_krawedzi = s[1]
    for i in range(liczba_krawedzi):
        s = list(map(int, file.readline().split()))
        ans.append(s)
    czy_jest_cykl = sprawdz_czy_jest_cykl(ans)
    if czy_jest_cykl:
        print()
        print("GRAF POSIADA CYKL")
        print("WYKONYWANIE PROGRAMU ZOSTAJE PRZERWANE")
    file.close()



while True:
    if czy_jest_cykl:
        break
    a = '0'
    while a != '1' and a != '2' and a != '3' and a != '4':
        print()
        print("     Wybierz strukture:")
        print("     - 1 - Macierz sasiedztwa")
        print("     - 2 - Lista nastepnikow")
        print("     - 3 - Macierz grafu")
        print("     - 4 - Wyjscie z programu")
        a = input('--> ')
        print()
    if a == '4':
        print('Bye Bye')
        break
    elif b == '1':
        if a == '1':
            # MACIERZ SASIEDZTWA Z KLAWIATURY
            macierz = stworz_macierz_sasiedztwa(dane_wprowadzone_przez_uzytkownika)
            print('-----------------------------')
            print('Struktura macierzy sasiedztwa')
            print('-----------------------------')
            for i in macierz:
                print(i)
            print('-----------------------------')
            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
            if c == '1':
                macierz_sasiedztwa_usuw_zer_st(macierz.copy())
            else:
                macierz_sasiedztwa_DFS(macierz.copy())

        elif a == '2':
            # LISTA NASTEPNIKOW Z KLAWIATURY
            print("SPRAWDZIC TWORZENIE LISTY NASTEPNIKOW Z KLAWIATURY!!!!!")
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
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
            if c == '1':
                lista_nastepnikow_przejdzn_metoda_zerowych(lista_nastepnikow.copy())
            else:
                lista_nastepnikow_przejdz_metoda_DFS(lista_nastepnikow.copy())

        elif a == '3':
            # MACIERZ GRAFU Z KLAWIATURY
            macierz_grafu = macierz_grafu_stworz_od_uzytkownika(dane_wprowadzone_przez_uzytkownika)
            print('------------------------')
            print('Struktura macierzy grafu')
            print('------------------------')
            for i in range(len(macierz_grafu)):
                print(i, ':', macierz_grafu[i])
            print('------------------------')
            c = '0'
            while c != '1' and c != '2':
                print()
                print("Wybierz przejscie przez graf:")
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
                print()
            if c == '1':
                macierz_grafu_przejdz_metoda_zerowych(macierz_grafu)
            else:
                macierz_grafu_przejdz_DSF(macierz_grafu)


    elif b == '2':
        if a == '1':
            # MACIERZ SASIEDZTWA Z PLIKU
            macierz = stworz_macierz_sasiedztwa_z_pliku()
            print('-----------------------------')
            print('Struktura macierzy sasiedztwa')
            print('-----------------------------')
            for i in macierz:
                print(i)
            print('-----------------------------')

            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
            if c == '1':
                macierz_sasiedztwa_usuw_zer_st(macierz)
            else:
                macierz_sasiedztwa_DFS(macierz)

        elif a == '2':
            # LISTA NASTEPNIKOW Z PLIKU
            lista_nastepnikow = stworz_liste_nastepnikow_z_pliku()
            print('---------------------------')
            print('Struktura listy nastepnikow')
            print('---------------------------')
            for i in range(len(lista_nastepnikow)):
                print(i, ':', lista_nastepnikow[i])
            print('---------------------------')

            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
            if c == '1':
                lista_nastepnikow_przejdzn_metoda_zerowych(lista_nastepnikow.copy())
            else:
                lista_nastepnikow_przejdz_metoda_DFS(lista_nastepnikow.copy())

        elif a == '3':
            # MACIERZ GRAFU Z PLIKU
            macierz_grafu = macierz_grafu_stworz_z_pliku()
            print('------------------------')
            print('Struktura macierzy grafu')
            print('------------------------')
            for i in range(len(macierz_grafu)):
                print(i, ':', macierz_grafu[i])
            print('------------------------')
            c = '0'
            while c != '1' and c != '2':
                print("Wybierz przejscie przez graf:")
                print("- 1 - z usuwaniem wierzchołków o zerowym stopniu wejściowym")
                print("- 2 - wykorzystaniem procedury przechodzenia w głąb (DFS)")
                c = input()
            if c == '1':
                macierz_grafu_przejdz_metoda_zerowych(macierz_grafu)
            else:
                macierz_grafu_przejdz_DSF(macierz_grafu)