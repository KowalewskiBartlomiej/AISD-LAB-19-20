import datetime
import sys
sys.setrecursionlimit(999999)

def insertionSort(arr):
    liczba_krokow = 0
    liczba_porownan = 0
    liczba_zamian = 0
    countTime = datetime.datetime.now()
    #print("Next Steps (insertion sort):")
    for i in range(1, len(arr), 1):
        for j in range(i, 0, -1):
            #print(countSteps, ".", arr)
            if (arr[j-1] >= arr[j]):
                liczba_porownan+=1
                break
            else:
                liczba_porownan+=1
                liczba_zamian+=1
                tmp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = tmp
    liczba_krokow+=liczba_porownan+liczba_zamian
    print(arr)
    print("Liczba kroków(ogółem):", liczba_krokow)
    print("Liczba porównań:", liczba_porownan)
    print("Liczba zamian:", liczba_zamian)
    print("Czas:", datetime.datetime.now() - countTime)
    return arr

def knuth(len_arr):
    h = 1
    while h < len_arr:
        h = 3*h + 1
    h = h//9
    return h

def shellSort(arr, reverse=True):
    countTime = datetime.datetime.now()
    liczba_krokow = 0
    liczba_zamian = 0
    liczba_porownan = 0
    len_arr = len(arr)
    gap = knuth(len_arr)
    while gap > 0:
        for i in range(gap, len_arr):
            insert = arr[i]
            j = i
            liczba_porownan += 1
            while(j >= gap and arr[j-gap] < insert):
                arr[j] = arr[j-gap]
                j -= gap
                liczba_zamian += 1
            arr[j] = insert
        print("Przyrost Knutha:", gap)
        gap //= 3
    print(arr)
    print("Czas:", datetime.datetime.now() - countTime)
    print("Liczba kroków(ogółem):", liczba_zamian + liczba_porownan)
    print("Liczba zamian:", liczba_zamian)
    print("Liczba porownan:", liczba_porownan)

def heapify(arr, n, i):
    # Find largest among root and children
    liczba_porownan = 0
    liczba_zamian = 0
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    liczba_porownan+=1
    if l < n and arr[i] > arr[l]:
        smallest = l
        liczba_zamian+=1
    liczba_porownan+=1
    if r < n and arr[smallest] > arr[r]:
        smallest = r
        liczba_zamian+=1

    # If root is not largest, swap with largest and continue heapifying
    liczba_porownan+=1
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        liczba_zamian+=1
    return [liczba_porownan, liczba_zamian]

def heapSort(arr):
    n = len(arr)
    countTime = datetime.datetime.now()
    liczba_krokow = 0
    liczba_zamian = 0
    liczba_porownan = 0
    # Build max heap
    for i in range(n-1, -1, -1):
        liczba_krokow += heapify(arr, n, i)[0]+heapify(arr, n, i)[1]
        liczba_porownan += heapify(arr, n, i)[0]
        liczba_zamian += heapify(arr, n, i)[1]
    for i in range(n - 1, 0, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]
        liczba_zamian+=1
        liczba_krokow+=1
        # heapify root element
        liczba_krokow += heapify(arr, i, 0)[0]+heapify(arr, i, 0)[1]
        liczba_zamian += heapify(arr, i, 0)[1]
        liczba_porownan += heapify(arr, i, 0)[0]
    print(arr)
    print("Czas:", datetime.datetime.now() - countTime)
    print("Liczba kroków(ogółem):", liczba_krokow)
    print("Liczba zamian:", liczba_zamian)
    print("Liczba porownan:", liczba_porownan)

def mergeSort(tab):
    countTime = datetime.datetime.now()
    tab = mergeSortRec(tab)
    print("Time:", datetime.datetime.now() - countTime)
    print("Ans:", tab)

def mergeSortRec(tab):
    if len(tab) > 1:
        middle = len(tab) // 2
        left = tab[:middle]
        right = tab[middle:]
        mergeSortRec(left)
        mergeSortRec(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]: #TU
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1
    return tab

def quickSortt(tab):
    countTime = datetime.datetime.now()
    liczba_porownan, liczba_zamian, liczba_krokow, arr = quickSort(tab, 0, len(tab)-1)
    print(arr)
    print("Liczba kroków(ogółem):", liczba_krokow)
    print("Liczba porównań:", liczba_porownan)
    print("Liczba zamian:", liczba_zamian)
    print("Czas:", datetime.datetime.now() - countTime)

def partition(arr, low, high):
    liczba_porownan = 0
    liczba_zamian = 0
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        liczba_porownan += 1
        if arr[j] >= pivot: #TU
            liczba_zamian += 1
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print("--> ", arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print("---> ", arr)
    return [(i + 1), liczba_porownan, liczba_zamian]

def quickSort(arr, low, high):
    liczba_porownan = 0
    liczba_zamian = 0
    liczba_krokow = 0
    if low < high:
        print("-> ", arr)
        pi, liczba_porownan_tmp, liczba_zamian_tmp = partition(arr, low, high)
        print("pivot:", arr[pi])
        liczba_porownan += liczba_porownan_tmp
        liczba_zamian += liczba_zamian_tmp
        liczba_krokow += liczba_zamian_tmp + liczba_porownan_tmp
        liczba_porownan_tmp, liczba_zamian_tmp, s, x = quickSort(arr, low, pi - 1)
        liczba_porownan += liczba_porownan_tmp
        liczba_zamian += liczba_zamian_tmp
        liczba_krokow += liczba_zamian_tmp + liczba_porownan_tmp
        liczba_porownan_tmp, liczba_zamian_tmp, s, x = quickSort(arr, pi + 1, high)
        liczba_porownan += liczba_porownan_tmp
        liczba_zamian += liczba_zamian_tmp
        liczba_krokow += liczba_zamian_tmp + liczba_porownan_tmp
    return [liczba_porownan, liczba_zamian, liczba_krokow, arr]