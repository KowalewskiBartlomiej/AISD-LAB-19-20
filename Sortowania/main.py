from generate_data import *
from sort import *
from import_from_txt import *

interval = []

b = '0'
while b != '1' and b != '2' and b != '3':
    print("Choose input method:")
    print("- 1 - My input")
    print("- 2 - Generate input")
    print("- 3 - Import from txt")
    b = '2'

if b != '3':
    n = int(input("How many elements: "))

if b == '1':
    for i in range(n):
        interval.append(int(input(str(i + 1) + " element: ")))
elif b == '2':
    print("Choose input form:")
    print("- 1 - Ascending")
    print("- 2 - Descending")
    print("- 3 - Random")
    print("- 4 - V-form")
    print("- 5 - A-form")
    c = '5'
    if c == '2':
        interval = draw_data(n, 10, 15000)
        interval = insertionSort(interval)
        print(interval)
    elif c == '1':
        interval = draw_data(n, 10, 15000)
        interval = insertionSort(interval)
        interval.reverse()
        print(interval)
    elif c == '3':
        interval = draw_data(n, 10, 15000)
        print(interval)
    elif c == '5':
        interval = draw_data(n, 10, 15000)
        middle = len(interval) // 2
        left = interval[:middle]
        right = interval[middle:]
        left = insertionSort(left)
        left.reverse()
        right = insertionSort(right)
        interval = left + right
        print(interval)
    elif c == '4':
        interval = draw_data(n, 10, 15000)
        middle = len(interval) // 2
        left = interval[:middle]
        right = interval[middle:]
        left = insertionSort(left)
        right = insertionSort(right)
        right.reverse()
        interval = left + right
        print(interval)
    else:
        print("! Input intiger form 1 to 5 !")
elif b == '3':
    interval = readFromTxt()

print("Choose sort method: ")
print("- 1 - Merge Sort")
print("- 2 - Heap Sort")
print("- 3 - Insertion Sort")
print("- 4 - Shell Sort z przyrostami Knutha")
print("- 5 - Quick Sort w wersji rekurencyjnej")
a = '4'
if a == '1':
    mergeSort(interval)
elif a == '2':
    heapSort(interval)
elif a == '3':
    insertionSort(interval)
elif a == '4':
    shellSort(interval)
elif a == '5':
    quickSortt(interval)
else:
    print("! Input intiger form 1 to 5 !")