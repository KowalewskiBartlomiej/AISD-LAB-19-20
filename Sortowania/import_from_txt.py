def readFromTxt():
    arr = []
    tekst = open("inpu.txt")
    data = tekst.read()
    print(data)
    arr = list(map(int, data.split()))
    return arr