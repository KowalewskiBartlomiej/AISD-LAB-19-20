ans = []
odwiedzone_wierzcholki = []
czy_znaleziono = False

def stworz_macierz_sasiedztwa_nieskierowana_z_klawiatury(dane_od_uzytkownika):
    liczba_wierz = dane_od_uzytkownika[0][0]
    liczba_kraw = dane_od_uzytkownika[0][1]
    dane_od_uzytkownika = dane_od_uzytkownika[1:]
    tmp = []
    ans = []

    for i in range(liczba_wierz):
        tmp.append(0)
    for i in range(liczba_wierz):
        ans.append(tmp.copy())

    for s in dane_od_uzytkownika:
        if s[0] < s[1]:
            ans[s[0]][s[1]] = 1
            ans[s[1]][s[0]] = 1
        elif s[0] > s[1]:
            ans[s[1]][s[0]] = 1
            ans[s[0]][s[1]] = 1
        else:
            print("ERROR")

    return ans

def stworz_macierz_sasiedztwa_nieskierowana_z_pliku(nazwa_pliku):
    file = open(nazwa_pliku, 'r')
    s = list(map(int, file.readline().split()))
    liczba_wierz = s[0]
    liczba_kraw = s[1]
    tmp = []
    ans = []
    for i in range(liczba_wierz):
        tmp.append(0)
    for i in range(liczba_wierz):
        ans.append(tmp.copy())
    for i in range(liczba_kraw):
        s = list(map(int, file.readline().split()))
        if s[0] < s[1]:
            ans[s[0]][s[1]] = 1
            ans[s[1]][s[0]] = 1
        elif s[0] > s[1]:
            ans[s[1]][s[0]] = 1
            ans[s[0]][s[1]] = 1
        else:
            print("ERROR")

    file.close()
    return ans

def stworz_liste_nastepnikow_z_pliku(nazwa_pliku):
    file = open(nazwa_pliku, 'r')
    s = list(map(int, file.readline().split()))
    liczba_wierz = s[0]
    liczba_kraw = s[1]
    tmp = []
    ans = []

    for i in range(s[0]):
        ans.append([])

    for i in range(liczba_kraw):
        s = list(map(int, file.readline().split()))
        ans[s[0]].append(s[1])

    for i in range(liczba_wierz):
        ans[i] = insertionSort(ans[i])

    file.close()
    return ans

def insertionSort(arr):
    if len(arr) == 0:
        return arr
    if len(arr) == 1:
        return arr
    for i in range(1, len(arr), 1):
        for j in range(i, 0, -1):
            if (arr[j-1] <= arr[j]):
                break
            else:
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
    return arr


# MACIERZ SASIEDZTWA CYKL HAMILTONA
def znajdz_cykl_hamiltona_macierz_sasiedztwa_REC(macierz, index_aktualnego):
    #print('Aktualny wierzcholek:', index_aktualnego)
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    if czy_znaleziono:
        return
    # DODAJE AKTUALNY WIERZCHOLEK NA STOS ODPOWIEDZI
    odwiedzone_wierzcholki.append(index_aktualnego)

    # SPRAWDZAM CZY CZY WSZYSTKIE WIERZCHOLKI SA DODANE NA LISTE ODPOWIEDZI
    if len(odwiedzone_wierzcholki) < len(macierz):
        # JESZCZE NIE MA SCIEZKI HAMILTONA, SZYKAMY DALEJ
        for i in range(len(macierz)):
            # W PONIŻSZYCH INSTRUKCJACH WARUNKOWYCH SPRAWDZAMY, CZY ISTNIEJE NASTĘPNIK (i), KTÓRY NIE ZNAJDUJE SIĘ NA LIŚCIE (odwiedzone_wierzchołki)
            if macierz[index_aktualnego][i] == 1:
                if i not in odwiedzone_wierzcholki:
                    # JEŚLI ZNAJDUJEMY TAKI NASTĘPNIK (i) WYWOŁUJEMY DLA NIEGO REKURENCYJNIE FUNKCJĘ
                    znajdz_cykl_hamiltona_macierz_sasiedztwa_REC(macierz, i)
    else:
        #MAMY WSZYSTKIE WIERZCHOLKI NA LIŚCIE (odwiedzone_wierzchołki), SPRAWDZAMY CZY OSTATNI WIERZCHOLEK NA STOSIE JEST POLACZONY KRAWEDZIA Z PIERWSZYM WIERZCHLKIEM NA STOSIE
        if macierz[index_aktualnego][odwiedzone_wierzcholki[0]] == 1:
            # JEŚŁI JEST TO ZNALEŹLIŚMY CYKL HAMILTONA
            ans = odwiedzone_wierzcholki
            czy_znaleziono = True
            return
        #else:
            # JESLI NIE TO ZNALEZLISMY JEDYNIE SCIEZKE HAMILTONA
            #print("BRAK CYKLU HAMILTONA")
            #return

    # WIERZCHOŁEK NIE MA NASTĘPNIKÓW, NIE ZNALEŹLIŚMY DO TEJ PORY ŚCIEŻKI HAMILTONA, WIĘC USUWAMY TEN WIERZCHOŁEK Z LISTY (odwiedzone_wierzchołki)
    odwiedzone_wierzcholki = odwiedzone_wierzcholki[0:-1]

def znajdz_cykl_hamiltona_macierz_sasiedztwa(macierz):
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    czy_znaleziono= False
    odwiedzone_wierzcholki = []
    ans = None
    znajdz_cykl_hamiltona_macierz_sasiedztwa_REC(macierz, 0)
    if ans == None:
        print()
        print("W GRAFIE NIE ZNALEZIONO CYKLU HAMILTONA (MACIERZ SASIEDZTWA)")
        print()
    else:
        print()
        print("ZNALEZIONO CYKL HAMILTONA (MACIERZ SASIEDZTWA)")
        print(ans)
        print()


# LISTA NASTEPNIKOW CYKL HAMILTONA
def znajdz_cykl_hamiltona_lista_nastepnikow_REC(lista_nastepnikow, index_aktualnego):
    #print('Aktualny wierzcholek:', index_aktualnego)
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    if czy_znaleziono:
        return
    # DODAJE AKTUALNY WIERZCHOLEK NA STOS
    odwiedzone_wierzcholki.append(index_aktualnego)

    # SPRAWDZAM, CZY LICZBA ELEMENRTOW NA STOSIE JEST MNIEJSZA OD LICZBY ELEMENTOW W GRAFIE
    if (len(odwiedzone_wierzcholki) < len(lista_nastepnikow)):
        # JESLI JEST MNIEJSZA PRZECHODZE ITERACYJNIE DO NASTĘPNIKOW DANEGO WIERZCHOLKA
        for i in lista_nastepnikow[index_aktualnego]:
            # SPRAWDZAM, CZY WIERZCHOŁEK DO KTÓREGO ZAMIERZAM SIĘ UDAĆ NIE ZOSTAŁ JUŻ UŻYTY (CZY NIE ZNAJDUJE SIĘ NA STOSIE)
            if i not in odwiedzone_wierzcholki:
                # JEŚLI NIE ZNAJDUJE SIĘ NA STOSIE WYWOŁUJĘ FUNKCJĘ REKURENCYJNIE PODAJĄC LISTĘ NASTĘPNIKÓW I NASTĘPNIK NA KTÓRYM ZAMIERZAM SIĘ USTAWIĆ
                znajdz_cykl_hamiltona_lista_nastepnikow_REC(lista_nastepnikow, i)
    else:
        # JEŚLI LICZBA ELEMENRTOW NA STOSIE JEST RÓWNA LICZBY ELEMENTOW W GRAFIE
        # SPRAWDZAM CZY NASTĘPNIKIEM OSTATNIEGO ELEMENTU NA STOSIE JEST PIERWSZY ELEMENT NA STOSIE
        if odwiedzone_wierzcholki[0] in lista_nastepnikow[index_aktualnego]:
            # JEŚLI TAK JEST TO ZNALEŹLIŚMY CYKL HAMILTONA
            ans = odwiedzone_wierzcholki
            czy_znaleziono = True
            return
        #else:
            # JEŚLI NIE TO NIE ZNALEŹLIŚMY ŚCIEŻKĘ HAMILTONA (KTÓRA NIE JEST ODPOWIEDZIĄ >CYKLEM<)
            #print("BRAK CYKLU HAMILTONA, TYLKO SCIEZKA")
            #return

    # USUWAM WIERZCHOŁEK NA KTÓRYM JESTEM USTAWIONY ZE STOSU
    odwiedzone_wierzcholki = odwiedzone_wierzcholki[0:-1]

def znajdz_cykl_hamiltona_lista_nastepnikow(lista_nastepnikow):
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    czy_znaleziono = False
    ans = None
    odwiedzone_wierzcholki = []
    znajdz_cykl_hamiltona_lista_nastepnikow_REC(lista_nastepnikow, 0)
    if ans == None:
        print()
        print("W GRAFIE NIE ZNALEZIONO CYKLU HAMILTONA (LISTA NASTEPNIKOW)")
        print()
    else:
        print()
        print("ZNALEZIONO CYKL HAMILTONA (LISTA NASTEPNIKOW)")
        print(ans)
        print()


# MACIERZ SASIEDZTWA CYKL EULERA
def znajdz_cykl_eulera_macierz_sasiedztwa_REC(macierz, index_aktualnego):
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    if czy_znaleziono:
        return

    #DODAJE WIERZCHOLEK NA KTORYM SIE ZNAJDUJE NA STOS
    odwiedzone_wierzcholki.append(index_aktualnego)

    # SPRAWDZAM CZY WSZYSTKIE KRAWEDZIE ZOSTALY USUNIETE POPRZEZ SPRAWDZENIE KAZDEJ KOMORKI MACIERZY (CZY JEJ WARTOSC JEST ROWNA ZERO)
    czy_usunieto_wszystkie_krawedzie = True
    for i in macierz:
        for j in i:
            if j == 1:
                # JESLI NIE TO DO ZMIENNEJ BOOL PRZYPISUJE FALSE I PRZERYWAM WYKONYWANIE PETLI
                czy_usunieto_wszystkie_krawedzie = False
                break


    if not czy_usunieto_wszystkie_krawedzie:
        # JESLI NIE WSZYSTKIE KRAWEDZIE ZOSTALY USUNIETE
        # DO ZMEINNEJ TYMCZASOWEJ ZAPISUJE WIERSZ Z MACIERZY SASIEDZTWA O INDEKSIE WIERZCHOLKA NA KTORYM SIE ZNAJDUJE W CELU USTALENIA SASIADOW
        tmp = macierz[index_aktualnego]
        # WYKONUJE PETLE DLA KAZDEGO ELEMENTU W STRUKTURZE DANEGO WIERSZA
        for i in range(len(tmp)):
            # SPRAWDZAM CZY WIERZCHOLEK O INDEKSIE i JEST SASIADEM WIERZCHOLKA NA KTORYM SIE ZNAJDUJEMY
            if tmp[i] == 1:
                # JESLI TAK TO USUWAM TAKIE POLACZENIE Z MACIERZY SASIEDZTWA
                macierz[index_aktualnego][i] = 0
                macierz[i][index_aktualnego] = 0
                # WYKONUJE REKURENCYJNIE FUNKCJE DLA MACIERZY (POMNIEJSZONEJ O DANY LUK) I SASIADA O INDEKSIE i
                znajdz_cykl_eulera_macierz_sasiedztwa_REC(macierz, i)
                # JESLI WYKONYWANIE REKURENCYJNE ZAKONCZYLO SIE NIEPOWODZENIEM TO PRZYWRACAM POPRZEDNI STAN MACIERZY SASIEDZTWA POPRZEZ DODANIE Z POWROTEM DANEGO ŁUKU
                macierz[index_aktualnego][i] = 1
                macierz[i][index_aktualnego] = 1
    else:
        # JESLI WSZYSTKIE LUKI ZOSTALY USUNIETE Z MACIERZY
        # SPRAWDZAM CZY OSTATNI WIERZCHOLEK NA STOSIE JEST ROWNY OSTATNIEMY
        if odwiedzone_wierzcholki[0] == odwiedzone_wierzcholki[-1]:
            # JESLI TAK TO PRZYPISUJE DO ZMIENNEJ PRZECHOWUJACEJ ODPOWIEDZ AKTUALNY STOS
            czy_znaleziono = True
            ans = odwiedzone_wierzcholki
            return
        #else:
            #return

    # USUWAM WIERZCHOLEK ZE STOSU JESLI NIE MA WIECEJ LUKOW WYCHODZACYCH Z TEGO WIERZCHOLKA
    odwiedzone_wierzcholki = odwiedzone_wierzcholki[0:-1]

def znajdz_cykl_eulera_macierz_sasiedztwa(macierz):
    global odwiedzone_krawedzie, czy_znaleziono, ans
    czy_znaleziono = False
    odwiedzone_krawedzie = []
    ans = None
    znajdz_cykl_eulera_macierz_sasiedztwa_REC(macierz, 0)
    if ans == None or ans == []:
        print()
        print("W GRAFIE NIE ZNALEZIONO CYKLU EULERA (MACIERZ SASIEDZTWA)")
        print()
    else:
        print()
        print("ZNALEZIONO CYKL EULERA (MACIERZ SASIEDZTWA)")
        print(ans)
        print()


# LISTA NASTEPNIKOW CYKL EULERA
def znajdz_cykl_eulera_lista_nastepnikow_REC(lista_nastepnikow, index_aktualnego):
    global odwiedzone_wierzcholki, czy_znaleziono, ans
    odwiedzone_wierzcholki.append(index_aktualnego)
    # SPRAWDZAM CZY ODPOWIEDZ JEST JUZ ZNALEZIONA
    if czy_znaleziono:
        # JESLI TAK PRZERYWAM WYKONYWANIE FUNKCJI REKURENCYJNEJ
        return

    # SPRAWDZAM CZY WSZYSTKIE NASTEPNIKI ZOSTALY USUNIETE Z LISTY NASTEPNIKOW
    czy_usunieto_wszystkie_krawedzie = True
    for i in lista_nastepnikow:
        if len(i) > 0:
            czy_usunieto_wszystkie_krawedzie = False
            break


    if not czy_usunieto_wszystkie_krawedzie:
        # JESLI WSZYSTKIE NASTEPNIKI ZOSTALY USUNIETE Z LISTY NASTEPNIKOW TO WYKONUJE:
        # DO ZMIENNEJ POMOCNICZEJ TMP PRZYPISUJE SKOPIOWANA STRUKTURE LISTY NASTEPNIKOW DLA WIERZCHOLKA NA KTORYM SIE ZNAJDUJE
        tmp = lista_nastepnikow[index_aktualnego].copy()
        # DLA KAZDEGO NASTEPIKA WIERZCHOLKA NA KTORYM SIE ZNAJDUJE WYKONUJE:
        for i in tmp:
            # USUWAM Z LISTY NASTEPNIKOW WIERZCHOLKA NA KTORYM SIE ZNAJDUJE WIERZCHOLEK DO KTOREGO SIE UDAJE I TA STRUKTURE PRZEKAZUJE JAKO PARAMETR LISTY NASTEPNIKOW
            # PRZY WYWOLANIU REKURENCYJNYM METODY
            lista_nastepnikow[index_aktualnego].remove(i)
            znajdz_cykl_eulera_lista_nastepnikow_REC(lista_nastepnikow, i)
            # JESLI WIERZCHOLEK NIE JEST TYM KTOREGO SZUKAMY DODAJEMY GO Z POWROTEM DO LISTY NASTEPNIKOW WIERZCHOLKA NA KTORYM SIE ZNAJDUJEMY
            lista_nastepnikow[index_aktualnego].append(i)
    else:
        # JEZLI WSZYSTKIE KRAWEDZIE ZOSTALY USUNIETE
        #SPRAWDZAM CZY PIERWSZY WIERZCHOLEK NA STOSIE JEST ROWNY OSTATNIEMU WIERZCHOLKOWI NA STOSIE
        if odwiedzone_wierzcholki[0] == odwiedzone_wierzcholki[-1]:
            # JESLI TAK TO ZNALEZLISMY CYKL EULERA I ODPOWIEDZ PRZYPISUJEMY DO ZMIENNEJ ans
            czy_znaleziono = True
            ans = odwiedzone_wierzcholki
            return
        #else:
            # JESLI NIE TO ZNALEZLISMY SCIEZKE EULERA SZUKAMY DALEJ
            #return

    odwiedzone_wierzcholki = odwiedzone_wierzcholki[0:-1]

def znajdz_cykl_eulera_lista_nastepnikow(lista_nastepnikow):
    global odwiedzone_wierzcholki, ans, czy_znaleziono
    czy_znaleziono = False
    ans = None
    odwiedzone_wierzcholki = []
    znajdz_cykl_eulera_lista_nastepnikow_REC(lista_nastepnikow, 0)
    if ans == None:
        print()
        print("W GRAFIE NIE ZNALEZIONO CYKLU EULERA (LISTA NASTEPNIKOW)")
        print()
    else:
        print()
        print("ZNALEZIONO CYKL EULERA (LISTA NASTEPNIKOW)")
        print(ans)
        print()