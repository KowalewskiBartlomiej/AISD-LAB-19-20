# KLASY
class Przedmiot:
    def __init__(self, id, weight, price):
        self.Id = id
        self.Weight = weight
        self.Price = price

    def WypiszPrzedmiot(self):
        print("ID:", self.Id, "Waga:", self.Weight, "Wartość:", self.Price)

    def WspolczynnikOplacalnosci(self):
        return self.Price / self.Weight

class RozwiazanieAW:
    def __init__(self, listaPrzedmiotow, maksObjPlecaka, binarnaTablica):
        self.BinarnaTablica = binarnaTablica
        self.ListaPrzedmiotow = listaPrzedmiotow
        self.MaksymalnaObjetoscPlecaka = maksObjPlecaka

    def CzyMiesciSieDoPlecaka(self):
        suma = 0
        for i in range(len(self.ListaPrzedmiotow)):
            if self.BinarnaTablica[i] == '1':
                suma += self.ListaPrzedmiotow[i].Weight
        return suma <= self.MaksymalnaObjetoscPlecaka

    def ObliczSumeWagPrzedmiotow(self):
        suma = 0
        for i in range(len(self.ListaPrzedmiotow)):
            if self.BinarnaTablica[i] == '1':
                suma += self.ListaPrzedmiotow[i].Weight
        return suma

    def ObliczSumeWartosciPrzedmiotow(self):
        suma = 0
        for i in range(len(self.ListaPrzedmiotow)):
            if self.BinarnaTablica[i] == '1':
                suma += self.ListaPrzedmiotow[i].Price
        return suma

    def WypiszPrzypadek(self):
        print(self.BinarnaTablica)

# TWORZENIE LISTY PRZEDMIOTÓW
def stworzListePrzedmiotowKlawiatura(daneKlawiatura):
    iloscPrzedmiotow = daneKlawiatura[0][0]
    objetoscPlecaka = daneKlawiatura[0][1]
    daneKlawiatura = daneKlawiatura[1:]
    listaPrzedmiotow = []

    for i in range(iloscPrzedmiotow):
        listaPrzedmiotow.append(Przedmiot(i, daneKlawiatura[i][0], daneKlawiatura[i][1]))

    return iloscPrzedmiotow, objetoscPlecaka, listaPrzedmiotow

def stworzListePrzedmiotowPliku(nazwaPliku):
    file = open(nazwaPliku, 'r')
    s = list(map(int, file.readline().split()))
    iloscPrzedmiotow = s[0]
    objetoscPlecaka = s[1]
    listaPrzedmiotow = []

    for i in range(iloscPrzedmiotow):
        s = list(map(int, file.readline().split()))
        if len(s) != 2:
            listaPrzedmiotow = None
            break
        if s[0] <= 0 or s[1] <= 0:
            listaPrzedmiotow = None
            break
        listaPrzedmiotow.append(Przedmiot(i, s[0], s[1]))

    file.close()
    return iloscPrzedmiotow, objetoscPlecaka, listaPrzedmiotow

# FUNKCJA REKURENCYJNA KONWERTUJĄCA LICZBĘ CAŁKOWITĄ DECYMALNĄ NA BINARNA
ans = ''
def convertToBinary(n):
    global ans
    ans += str(n % 2)
    if n > 1:
        convertToBinary(n//2)

# FUNKCJA TWORZĄCA BINARNIE WSZYSTKIE MOŻLIWE PRZYPADKI
def StworzBinarnaTabelePrzypadkow(n):
    global ans
    tabelaLancuchZnakow = []
    tabelaPrzypadkow = []
    for i in range(1, 2**n):
        ans = ''
        convertToBinary(i)
        ans += '0' * (n - len(ans))
        ans = ans[::-1]
        tabelaLancuchZnakow.append(ans)

    for i in tabelaLancuchZnakow:
        tabelaPrzypadkow.append(list(i))

    return tabelaPrzypadkow

# ALGORYTM WYCZERPUJĄCY
def AlgorytmWyczerpujacy(listaPrzedmiotow, objetoscPlecaka):
    binarnaTabelaPrzypadkow = StworzBinarnaTabelePrzypadkow(len(listaPrzedmiotow))
    rozwiazaniaAW = []

    counter = 0
    for przypadek in binarnaTabelaPrzypadkow:
        rozwiazaniaAW.append(RozwiazanieAW(listaPrzedmiotow, objetoscPlecaka, przypadek))

    wartoscSumyPrzedmiotowNajlepszego = -1
    indeksNajlepszegoRozwiazania = -1
    for rozwiazanie in rozwiazaniaAW:
        if rozwiazanie.CzyMiesciSieDoPlecaka():
            if rozwiazanie.ObliczSumeWartosciPrzedmiotow() > wartoscSumyPrzedmiotowNajlepszego:
                wartoscSumyPrzedmiotowNajlepszego = rozwiazanie.ObliczSumeWartosciPrzedmiotow()
                indeksNajlepszegoRozwiazania = rozwiazaniaAW.index(rozwiazanie)

    print("\n---------------------- ALGORYTM WYCZERPUJĄCY ----------------------------")
    print("W optymalnym rozwiazaniu do plecaka zmieszczą się następujące przedmioty:")
    for i in range(len(rozwiazaniaAW[indeksNajlepszegoRozwiazania].BinarnaTablica)):
        if rozwiazaniaAW[indeksNajlepszegoRozwiazania].BinarnaTablica[i] == '1':
            listaPrzedmiotow[i].WypiszPrzedmiot()
    print("o sumie wartości poszczególnych przedmiotów:", rozwiazaniaAW[indeksNajlepszegoRozwiazania].ObliczSumeWartosciPrzedmiotow())
    print("i łącznej wadze wszystkich przedmiotów:", rozwiazaniaAW[indeksNajlepszegoRozwiazania].ObliczSumeWagPrzedmiotow())
    print("-------------------------------------------------------------------------\n")

# ALGORYTM ZACHLANNY
def PosortujListePrzedmiotowPoWartosciNaJednostke(listaPrzedmiotow):
    posortowanaLista = []

    #poszukiwanyPrzedmiot = None
    #najwiekszaWartosc = -1

    while len(listaPrzedmiotow) > 0:
        poszukiwanyPrzedmiot = None
        najwiekszaWartosc = -1
        for i in range(len(listaPrzedmiotow)):
            if listaPrzedmiotow[i].WspolczynnikOplacalnosci() > najwiekszaWartosc:
                najwiekszaWartosc = listaPrzedmiotow[i].WspolczynnikOplacalnosci()
                poszukiwanyPrzedmiot = listaPrzedmiotow[listaPrzedmiotow.index(listaPrzedmiotow[i])]
        posortowanaLista.append(poszukiwanyPrzedmiot)
        listaPrzedmiotow.remove(poszukiwanyPrzedmiot)

    return posortowanaLista

def AlgorytmZachlanny(listaPrzedmiotow, objetoscPlecaka):
    listaPrzedmiotowPosortowana = PosortujListePrzedmiotowPoWartosciNaJednostke(listaPrzedmiotow.copy())
    listaPrzedmiotowWPlecaku = []
    sumaWagPrzedmiotowWPlecaku = 0
    sumaWartosciPrzedmiotowWPlecaku = 0
    print(listaPrzedmiotowPosortowana)
    licznik = 0
    while sumaWagPrzedmiotowWPlecaku + listaPrzedmiotowPosortowana[licznik].Weight <= objetoscPlecaka:
        listaPrzedmiotowWPlecaku.append(listaPrzedmiotowPosortowana[licznik])
        sumaWagPrzedmiotowWPlecaku += listaPrzedmiotowPosortowana[licznik].Weight
        sumaWartosciPrzedmiotowWPlecaku += listaPrzedmiotowPosortowana[licznik].Price
        licznik += 1
        if licznik == len(listaPrzedmiotow):
            break

    print("\n----------------------------- ALGORYTM ZACHLANNY -----------------------------------")
    print("W optymalnym/suboptymalnym rozwiazaniu do plecaka zmieszczą się następujące przedmioty:")
    for i in range(len(listaPrzedmiotowWPlecaku)):
        listaPrzedmiotowWPlecaku[i].WypiszPrzedmiot()
    print("o sumie wartości poszczególnych przedmiotów:", sumaWartosciPrzedmiotowWPlecaku)
    print("i łącznej wadze wszystkich przedmiotów:", sumaWagPrzedmiotowWPlecaku)
    print("------------------------------------------------------------------------------------\n")

# PROGRAMOWANIE DYNAMICZNE
macierzKosztow = []
def Bellman(i, j, listaPrzedmiotow):
    global macierzKosztow
    if i == 0 or j == 0:
        macierzKosztow[i][j] = 0
    elif listaPrzedmiotow[i-1].Weight > j:
        macierzKosztow[i][j] = macierzKosztow[i-1][j]
    elif listaPrzedmiotow[i-1].Weight <= j:
        if macierzKosztow[i-1][j] > macierzKosztow[i-1][j-listaPrzedmiotow[i-1].Weight] + listaPrzedmiotow[i-1].Price:
            macierzKosztow[i][j] = macierzKosztow[i-1][j]
        else:
            macierzKosztow[i][j] = macierzKosztow[i-1][j-listaPrzedmiotow[i-1].Weight] + listaPrzedmiotow[i-1].Price

def AlgorytmProgramowaniaDynamicznego(listaPrzedmiotow, objetoscPlecaka):
    global macierzKosztow

    macierzKosztow = []
    tmp = []
    for i in range(objetoscPlecaka + 1):
        tmp.append(None)

    for i in range(len(listaPrzedmiotow) + 1):
        macierzKosztow.append(tmp.copy())

    for i in range(len(macierzKosztow)):
        for j in range(len(macierzKosztow[0])):
            Bellman(i, j, listaPrzedmiotow)

    for i in range(len(macierzKosztow)):
        print(macierzKosztow[i])

    tablicaIdPrzedmiotowWPlecaku = []
    j = objetoscPlecaka
    for i in range(len(macierzKosztow) - 1, 0, -1):
        if macierzKosztow[i][j] != macierzKosztow[i - 1][j]:
            # PRZEDMIOT ZNAJDUJE SIE W PLECAKU
            tablicaIdPrzedmiotowWPlecaku.append(i - 1)
            j -= listaPrzedmiotow[i - 1].Weight

    sumaWagPoszczeglnychPrzedmiotow = 0
    sumaCenPoszczegolnychPrzedmiotow = 0
    #print("PRZEDMIOTY W TABLICY")
    for przedmiot in listaPrzedmiotow:
        if przedmiot.Id in tablicaIdPrzedmiotowWPlecaku:
            sumaWagPoszczeglnychPrzedmiotow += przedmiot.Weight
            sumaCenPoszczegolnychPrzedmiotow += przedmiot.Price

    print("\n--------------------- ALGORYTM PROGRAMOWANIA DYNAMICZNEGO ---------------------------")
    print("W optymalnym rozwiazaniu do plecaka zmieszczą się następujące przedmioty:")
    for przedmiot in listaPrzedmiotow:
        if przedmiot.Id in tablicaIdPrzedmiotowWPlecaku:
            przedmiot.WypiszPrzedmiot()
    print("o sumie wartości poszczególnych przedmiotów:", sumaCenPoszczegolnychPrzedmiotow)
    print("i łącznej wadze wszystkich przedmiotów:", sumaWagPoszczeglnychPrzedmiotow)
    print("------------------------------------------------------------------------------------\n")