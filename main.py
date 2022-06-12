ans = []



#           MACIERZ SĄSIEDZTWA

# TWORZENIE Z PLIKU
def stworz_macierz_sasiedztwa_z_pliku(nazwa_pliku):
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
            ans[s[1]][s[0]] = -1
        elif s[0] > s[1]:
            ans[s[1]][s[0]] = -1
            ans[s[0]][s[1]] = 1
        else:
            print("ERROR")

    file.close()
    return ans

# TWORZENIE Z KLAWIATURY
def stworz_macierz_sasiedztwa(dane_od_uzytkownika):
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
            ans[s[1]][s[0]] = -1
        elif s[0] > s[1]:
            ans[s[1]][s[0]] = -1
            ans[s[0]][s[1]] = 1
        else:
            print("ERROR")

    return ans

# USUWANIE WIERZCHOŁKA
def macierz_sasiedztwa_usuw_zer_st_usun_wierz(tab, index):
    for i in range(len(tab)):
        tab[index][i] = 0

    for i in range(len(tab)):
        tab[i][index] = 0

    return tab

# PRZEJŚCIE METODĄ ZEROWYCH WIERZCHOŁKÓW
def macierz_sasiedztwa_usuw_zer_st(tab):
    helper = []
    while True:
        for i in range(len(tab)):
            #print(i)
            if -1 not in tab[i] and i not in helper:
                helper.append(i)
                tab = macierz_sasiedztwa_usuw_zer_st_usun_wierz(tab, i)
                #print(i, ':', tab)
                break
                #print(i)
        if len(helper) == len(tab):
            break
    print()
    print('Przejscie przez macierz sasiedztwa metoda z usuwaniem wierzchołków o zerowym stopniu wejściowym:')
    print(helper)
    print()
    return helper

# PRZEJŚCIE METODĄ DFS (FUNKCJA REKURENCYJNA)
def macierz_sasiedztwa_DFS_REC(tab, index_wierz, stos):
    global ans
    if 1 not in tab[index_wierz] and len(stos) == 0:
        ans.insert(0, index_wierz)
        macierz_sasiedztwa_usuw_zer_st_usun_wierz(tab, index_wierz)
        return tab
    elif 1 not in tab[index_wierz] and len(stos) != 0:
        ans.insert(0, index_wierz)
        macierz_sasiedztwa_usuw_zer_st_usun_wierz(tab, index_wierz)
        macierz_sasiedztwa_DFS_REC(tab, stos[-1], stos[0:-2])
    else:
        stos.append(index_wierz)
        macierz_sasiedztwa_DFS_REC(tab, tab[index_wierz].index(1), stos)

# PRZEJŚCIE METODĄ DFS
def macierz_sasiedztwa_DFS(tab):
    global ans
    ans = []
    while True:
        if len(ans) != len(tab):
            for i in range(len(tab)):
                if i not in ans:
                    #print('Nowe przejscie: ', i)
                    macierz_sasiedztwa_DFS_REC(tab, i, [])
        else:
            break
    print()
    print('Przejscie przez macierz sasiedztwa metoda metodą DFS:')
    print(ans)
    print()
    return ans


            # LISTA NASTEPNIKOW


#           LISTA NASTĘPNIKÓW

# TWORZENIE Z KLAWIATURY # SPRAWDZIC!!!!!
def stworz_liste_nastepnikow(dane_od_uzytkownika):
    liczba_wierz = dane_od_uzytkownika[0][0]
    liczba_kraw = dane_od_uzytkownika[0][1]
    tmp = []
    ans = []
    dane_od_uzytkownika = dane_od_uzytkownika[1:]
    for i in range(liczba_wierz):
        ans.append([])

    for s in dane_od_uzytkownika:
        ans[s[0]].append(s[1])

    for i in range(liczba_wierz):
        ans[i] = insertionSort(ans[i])

    return ans

# TWORZENIE Z PLIKU
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

# USUWANIE WIERZCHOŁKA
def lista_nastepnikow_usun_wierzcholek(tab, index_wierzcholek):
    tab[index_wierzcholek] = []
    for i in tab:
        if index_wierzcholek in i:
            i.remove(index_wierzcholek)

    #print(tab)
    return tab

# PRZEJŚCIE METODĄ ZEROWYCH WIERZCHOŁKÓW
def lista_nastepnikow_przejdzn_metoda_zerowych(tab):
    ans = []
    while True:
        wierzcholek = -1
        for i in range(len(tab)):
            czy_to_ten = True
            for j in tab:
                if i in j:
                    czy_to_ten = False
                    break
            if czy_to_ten and i not in ans:
                wierzcholek = i
                break

        tab = lista_nastepnikow_usun_wierzcholek(tab, wierzcholek)
        ans.append(wierzcholek)

        if -1 in ans:
            return ans

        if len(ans) == len(tab):
            print()
            print('Przejscie przez lista nastepnikow metoda z usuwaniem wierzchołków o zerowym stopniu wejściowym:')
            print(ans)
            print()
            return ans

# PRZEJŚCIE METODĄ DFS (FUNKCJA REKURENCYJNA)
def lista_nastepnikow_przejdz_metoda_DFS_REC(tab, index_wierz, stos):
    global ans
    if len(tab[index_wierz]) == 0 and len(stos) == 0:
        ans.insert(0, index_wierz)
        lista_nastepnikow_usun_wierzcholek(tab, index_wierz)
        return tab
    elif len(tab[index_wierz]) == 0 and len(stos) != 0:
        ans.insert(0, index_wierz)
        lista_nastepnikow_usun_wierzcholek(tab, index_wierz)
        lista_nastepnikow_przejdz_metoda_DFS_REC(tab, stos[-1], stos[0:-2])
    else:
        stos.append(index_wierz)
        lista_nastepnikow_przejdz_metoda_DFS_REC(tab, tab[index_wierz][0], stos)

# PRZEJŚCIE METODĄ DFS
def lista_nastepnikow_przejdz_metoda_DFS(tab):
    global ans
    ans = []
    while True:
        if len(ans) != len(tab):
            for i in range(len(tab)):
                if i not in ans:
                    lista_nastepnikow_przejdz_metoda_DFS_REC(tab, i, [])
        else:
            break
    print()
    print('Przejscie przez liste nastepnikow metoda DFS:')
    print(ans)
    print()
    return ans

            #MACIERZ GRAFU



#           MACIERZ GRAFU

# TWORZENIE Z KLAWIATURY
def macierz_grafu_stworz_od_uzytkownika(dane_od_uzytkownika):
    liczba_wierz = dane_od_uzytkownika[0][0]
    liczba_krawedzi = dane_od_uzytkownika[0][1]


    lista_poprzednikow = lista_poprzednikow_stworz_z_klawiatury(dane_od_uzytkownika)
    #print('Poprzedniki:',lista_poprzednikow)
    lista_nastepnikow = stworz_liste_nastepnikow(dane_od_uzytkownika)
    #print('Nastepniki:',lista_nastepnikow)
    lista_brak_incydencji = lista_stworz_brak_incydencji(lista_nastepnikow, lista_poprzednikow)
    #print('Brak incydencji:',lista_brak_incydencji)

    ans = []
    tmp = []
    for i in range(liczba_wierz + 3):
        tmp.append(-1)
    for i in range(liczba_wierz):
        ans.append(tmp.copy())

    # WPISZ DANE DO KOLUMNY NASTEPNIKOW
    for i in range(liczba_wierz):
        if len(lista_nastepnikow[i]) > 0:
            ans[i][-3] = lista_nastepnikow[i][0]
        else:
            ans[i][-3] = -1

    for i in range(liczba_wierz):
        for j in lista_nastepnikow[i]:
            ans[i][j] = lista_nastepnikow[i][-1]


    # WPISZ DANE DO KOLUMNY POPRZEDNIKOW
    for i in range(liczba_wierz):
        if len(lista_poprzednikow[i]) > 0:
            ans[i][-2] = lista_poprzednikow[i][0]
        else:
            ans[i][-2] = -1

    for i in range(liczba_wierz):
        for j in lista_poprzednikow[i]:
            ans[i][j] = lista_poprzednikow[i][-1] + liczba_wierz

    # WPISZ DANE DO KOLUMNY BRAK INCYDENCJI
    for i in range(liczba_wierz):
        if len(lista_brak_incydencji[i]) > 0:
            ans[i][-1] = lista_brak_incydencji[i][0]
        else:
            ans[i][-1] = -1

    for i in range(liczba_wierz):
        for j in lista_brak_incydencji[i]:
            ans[i][j] = lista_brak_incydencji[i][-1] + (2 * liczba_wierz)

    for i in range(liczba_wierz):
        ans[i][i] = -1

    return ans

# TWORZENIE Z PLIKU
def macierz_grafu_stworz_z_pliku(nazwa_pliku):
    file = open(nazwa_pliku, 'r')
    s = list(map(int, file.readline().split()))
    liczba_wierz = s[0]
    liczba_krawedzi = s[1]

    lista_poprzednikow = lista_poprzednikow_stworz_z_pliku(nazwa_pliku)
    #print('Poprzedniki:',lista_poprzednikow)
    lista_nastepnikow = stworz_liste_nastepnikow_z_pliku(nazwa_pliku)
    #print('Nastepniki:',lista_nastepnikow)
    lista_brak_incydencji = lista_stworz_brak_incydencji(lista_nastepnikow, lista_poprzednikow)
    #print('Brak incydencji:',lista_brak_incydencji)

    ans = []
    tmp = []
    for i in range(liczba_wierz + 3):
        tmp.append(-1)
    for i in range(liczba_wierz):
        ans.append(tmp.copy())

    # WPISZ DANE DO KOLUMNY NASTEPNIKOW
    for i in range(liczba_wierz):
        if len(lista_nastepnikow[i]) > 0:
            ans[i][-3] = lista_nastepnikow[i][0]
        else:
            ans[i][-3] = -1

    for i in range(liczba_wierz):
        for j in lista_nastepnikow[i]:
            ans[i][j] = lista_nastepnikow[i][-1]


    # WPISZ DANE DO KOLUMNY POPRZEDNIKOW
    for i in range(liczba_wierz):
        if len(lista_poprzednikow[i]) > 0:
            ans[i][-2] = lista_poprzednikow[i][0]
        else:
            ans[i][-2] = -1

    for i in range(liczba_wierz):
        for j in lista_poprzednikow[i]:
            ans[i][j] = lista_poprzednikow[i][-1] + liczba_wierz

    # WPISZ DANE DO KOLUMNY BRAK INCYDENCJI
    for i in range(liczba_wierz):
        if len(lista_brak_incydencji[i]) > 0:
            ans[i][-1] = lista_brak_incydencji[i][0]
        else:
            ans[i][-1] = -1

    for i in range(liczba_wierz):
        for j in lista_brak_incydencji[i]:
            ans[i][j] = lista_brak_incydencji[i][-1] + (2 * liczba_wierz)

    for i in range(liczba_wierz):
        ans[i][i] = -1
    file.close()
    return ans

# USUWANIE WIERZCHOLKA
def macierz_grafu_usun_wierzcholek(tab, index_do_usuniecia):
    wielkosc_tablicy = len(tab)
    #print('macierz_grafu_usun_wierzcholek()', index_do_usuniecia)

    # UZUPELNIANIE GLOWEJ MACIERZY
    for i in range(wielkosc_tablicy):
        for j in range(wielkosc_tablicy):
            if tab[i][j] == index_do_usuniecia:
                tab[i][j] = tab[i][wielkosc_tablicy]

    # UZUPELNIENIE KOLUMNY Z LISTA NASTEPNIKOW
    for i in range(wielkosc_tablicy):
        if tab[i][wielkosc_tablicy] == index_do_usuniecia:
            index_do_wstawienia = tab[i][tab[i][wielkosc_tablicy]]
            tmp = tab[i][wielkosc_tablicy]
            for j in range(wielkosc_tablicy):
                if tab[i][j] == index_do_wstawienia and j != tmp:
                    tab[i][wielkosc_tablicy] = j
                    break
                else:
                    tab[i][wielkosc_tablicy] = -1



    # UZUPELNIANIE KOLUMNY Z LISTA POPRZEDNIKOW
    for i in range(wielkosc_tablicy):
        if tab[i][wielkosc_tablicy + 2] == index_do_usuniecia:
            index_do_wstawienia = tab[i][tab[i][wielkosc_tablicy + 2]]
            tmp = tab[i][wielkosc_tablicy + 2]
            for j in range(wielkosc_tablicy):
                if tab[i][j] == index_do_wstawienia and j != tmp:
                    tab[i][wielkosc_tablicy + 2] = j
                    break
                else:
                    tab[i][wielkosc_tablicy + 2] = -1


    # USUWANIE WIERZCHOLKA Z LISTY
    for i in range(len(tab[index_do_usuniecia])):
        tab[index_do_usuniecia][i] = -2

    for i in range(len(tab)):
        tab[i][index_do_usuniecia] = -2

    #print('--------------------------------------')
    #print(index_do_usuniecia)
    #for i in tab:
    #    print(i)

    return tab

# PRZEJSCIE METODA ZEROWYCH WIERZCHOLKOW
def macierz_grafu_przejdz_metoda_zerowych(tab):
    ans = []
    while len(ans) < len(tab):
        usuwany_index = -1
        for i in tab:
            if i[len(tab)] == -1:
                usuwany_index = tab.index(i)
        ans.insert(0, usuwany_index)
        tab = macierz_grafu_usun_wierzcholek(tab, usuwany_index)

    print()
    print('Przejscie przez macierz grafu metoda z usuwaniem wierzchołków o zerowym stopniu wejściowym:')
    print(ans)
    print()
    return ans

# PRZEJŚCIE METODĄ DFS (FUNKCJA REKURENCYJNA)
def macierz_grafu_przejdz_DSF_REC(tab, index_wierz, stos):
    global ans
    #print('ans',ans)
    if tab[index_wierz][len(tab)] != -1:
        stos.append(index_wierz)
        macierz_grafu_przejdz_DSF_REC(tab, tab[index_wierz][len(tab)], stos)
        #if tab[index_wierz][len(tab)] != 0:
        #    stos.append(index_wierz)
        #    macierz_grafu_przejdz_DSF_REC(tab, tab[index_wierz][len(tab)], [])
        #    ans.insert(0, index_wierz)
        #    tab = macierz_grafu_usun_wierzcholek(tab, index_wierz)
        #    return
    else:
        # print('insert: ', index_wierz)
        ans.insert(0, index_wierz)
        tab = macierz_grafu_usun_wierzcholek(tab, index_wierz)
        if len(stos) > 0:
            macierz_grafu_przejdz_DSF_REC(tab, stos[-1], stos[0:-2])
        else:
            if len(ans) == len(tab):
                return
            else:
                return

# PRZEJŚCIE METODĄ DFS
def macierz_grafu_przejdz_DSF(tab):
    global ans
    ans = []
    while True:
        if len(ans) != len(tab):
            for i in range(len(tab)):
                if i not in ans:
                    # print('Nowe przejscie: ', i)
                    macierz_grafu_przejdz_DSF_REC(tab, i, [])
        else:
            break

    print()
    print('Przejscie przez macierz grafu metoda DFS:')
    print(ans)
    print()
    return ans



#           DODATKOWO

def sprawdz_czy_jest_cykl(dane_od_uzytkownika):
    lista_nastepnikow = stworz_liste_nastepnikow(dane_od_uzytkownika)
    ans = []
    while True:
        wierzcholek = -1
        for i in range(len(lista_nastepnikow)):
            czy_to_ten = True
            for j in lista_nastepnikow:
                if i in j:
                    czy_to_ten = False
                    break
            if czy_to_ten and i not in ans:
                wierzcholek = i
                break

        tab = lista_nastepnikow_usun_wierzcholek(lista_nastepnikow, wierzcholek)
        ans.append(wierzcholek)

        if -1 in ans:
            return True

        if len(ans) == len(tab):
            break

    if -1 in ans:
        return True
    else:
        return False

def lista_poprzednikow_stworz_z_pliku(nazwa_pliku):
    file = open(nazwa_pliku, 'r')
    s = list(map(int, file.readline().split()))
    liczba_wierz = s[0]
    liczba_kraw = s[1]
    ans = []

    for i in range(liczba_wierz):
        ans.append([])

    for i in range(liczba_kraw):
        s = list(map(int, file.readline().split()))
        ans[s[1]].append(s[0])

    for i in range(liczba_wierz):
        ans[i] = insertionSort(ans[i])

    return ans

def lista_poprzednikow_stworz_z_klawiatury(dane_od_uzytkownika):
    liczba_wierz = dane_od_uzytkownika[0][0]
    liczba_kraw = dane_od_uzytkownika[0][1]
    ans = []
    dane_od_uzytkownika = dane_od_uzytkownika[1:]

    for i in range(liczba_wierz):
        ans.append([])

    for s in dane_od_uzytkownika:
        ans[s[1]].append(s[0])

    for i in range(liczba_wierz):
        ans[i] = insertionSort(ans[i])

    return ans

def lista_stworz_brak_incydencji(lista_nastepnikow, lista_poprzednikow):
    ans = []
    for i in range(len(lista_nastepnikow)):
        ans.append([])

    for i in range(len(ans)):
        for j in range(len(ans)):
            if j not in lista_nastepnikow[i] and j not in lista_poprzednikow[i] and i != j:
                ans[i].append(j)

    for i in range(len(ans)):
        ans[i] = sorted(ans[i])

    #print(ans)
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





#[[0, 1, 0, -1, 0, 0, 0], [-1, 0, -1, 1, 0, 0, 0], [0, 1, 0, 0, -1, 0, 1], [1, -1, 0, 0, 1, 0, 0], [0, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 1, 0, -1], [0, 0, -1, 0, 0, 1, 0]]

#print(stworz_macierz_sasiedztwa(liczba_kraw, liczba_wierz))
#print(macierz_sasiedztwa_DFS([[0, 1, -1, 1], [-1, 0, 0, 0], [1, 0, 0, 1], [-1, 0, -1, 0]]))
#print(lista_nastepnikow_usun_wierzcholek(stworz_liste_nastepnikow_z_pliku(), 3))
#[[0, -1, 1, -1, 0, -1], [1, 0, 1, -1, -1, 0], [-1, -1, 0, 0, -1, 0], [1, 1, 0, 0, 1, 0], [0, 1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0]]
#_, ans = macierz_sasiedztwa_usuw_zer_st([[0, -1, 1, -1, 0, -1], [1, 0, 1, -1, -1, 0], [-1, -1, 0, 0, -1, 0], [1, 1, 0, 0, 1, 0], [0, 1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0]])
#print(ans)

#[[0, 1, 0, -1, 0, 0, 0], [-1, 0, -1, 1, 0, 0, 0], [0, 1, 0, 0, -1, 0, 1], [1, -1, 0, 0, 1, 0, 0], [0, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 1, 0, -1], [0, 0, -1, 0, 0, 1, 0]]

#[[0, 1, 0, 1, 0, 0, 0, 0, 0], [-1, 0, 1, -1, 0, 0, 0, 0, 0], [0, -1, 0, 0, 1, 0, 0, 0, 0], [-1, 1, 0, 0, 0, 0, 0, -1, 0], [0, 0, -1, 0, 0, 1, 0, -1, 1], [0, 0, 0, 0, -1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, -1, -1], [0, 0, 0, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, -1, -1, 1, 0, 0]]
#print(stworz_macierz_sasiedztwa(liczba_kraw, liczba_wierz))
#macierz_sasiedztwa_usuw_zer_st([[0, 1, 0, -1, 0, 0, 0], [-1, 0, -1, 1, 0, 0, 0], [0, 1, 0, 0, -1, 0, 1], [1, -1, 0, 0, 1, 0, 0], [0, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 1, 0, -1], [0, 0, -1, 0, 0, 1, 0]])
#macierz = [[0, -1, 1, -1, 0, -1], [1, 0, 1, -1, -1, 0], [-1, -1, 0, 0, -1, 0], [1, 1, 0, 0, 1, 0], [0, 1, 1, -1, 0, -1], [1, 0, 0, 0, 1, 0]]

#macierz_sasiedztwa_usuw_zer_st([[0, 1, 0, -1, 0, 0, 0], [-1, 0, -1, 1, 0, 0, 0], [0, 1, 0, 0, -1, 0, 1], [1, -1, 0, 0, 1, 0, 0], [0, 0, 1, -1, 0, -1, 0], [0, 0, 0, 0, 1, 0, -1], [0, 0, -1, 0, 0, 1, 0]])