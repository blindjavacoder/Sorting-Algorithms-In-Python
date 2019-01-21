#!/usr/bin/python
import sys
import random
import time
import timeit
sys.setrecursionlimit(10000)
ctrI = 0
ctrM = 0
def Insertion_Sort( A ):
    global ctrI
    for j in range(1, len(A)):
        ctrI += 1
        anahtar = A[j]
        ctrI += 1
        i = j - 1
        ctrI += 1
        while i >= 0 and A[i] > anahtar :
            ctrI += 1
            A[i + 1] = A[i]
            ctrI += 1
            i = i - 1
            ctrI += 1
        A[i + 1] = anahtar
        ctrI += 1
def printIns( A ):
    length = len(A)
    print("--------------------------------------")
    print("%s Elements Array in Insertion Sort Algorithm " % length)
    from timeit import default_timer as timer
    start = timer()
    Insertion_Sort( A )
    end = timer()
    print( A )
    print("Counter : {0} Time : {1}".format(ctrI, (end - start)))
    print("--------------------------------------")
def Merge_Sort( A, p ,r):
    global ctrM
    if p < r :
        ctrM += 1
        q = int((p+r)/2)
        ctrM += 1
        Merge_Sort(A, p ,q)
        ctrM += 1
        Merge_Sort(A, q + 1, r)
        ctrM += 1
        Merge(A, p, q ,r)
        ctrM += 1
def Merge(A, p, q ,r):
    global ctrM
    n1 = int(q - p + 1)
    ctrM += 1
    n2 = int(r - q)
    ctrM += 1
    L = [None] * int(n1)
    ctrM += 1
    R = [None] * int(n2)
    ctrM += 1
    for i in range(0,n1):
        ctrM += 1
        L[i] = A[p + i]
        ctrM += 1
    for j in range(0,n2):
        ctrM += 1
        R[j] = A[q + j + 1]
        ctrM += 1
    i = 0
    ctrM += 1
    j = 0
    ctrM += 1
    k = p
    ctrM += 1
    for k in range(p, r):
        ctrM += 1
        if i < n1 and j < n2 :
            ctrM += 1
            if L[i] <= R[j]:
                ctrM += 1
                A[k] = L[i]
                ctrM += 1
                i += 1
                ctrM += 1
            else:
                ctrM += 1
                A[k] = R[j]
                ctrM += 1
                j += 1
                ctrM += 1
            k += 1
            ctrM += 1

def printMerge( A ):
    n = int(len(A))
    print("--------------------------------------")
    print("%s Elements Array in Merge Sort Algorithm " % n)
    from timeit import default_timer as timer
    start = timer()
    Merge_Sort(A, 0, n-1)
    end = timer()
    print("Counter : {0} Time : {1}".format(ctrM, (end - start)))
    print("--------------------------------------")
    print(A)

'''
def quickSort(A,b,s):
    if b < s :
        r = partition(A,b,s)
        #print(A)
        #print(r)
        quickSort(A,b,r-1)
        quickSort(A,r+1,s)
def partition (A,b,s):
    pivot = A[s]
    i = b - 1
    for j in range(b,s):
        if A[j] <= pivot:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i+1]
    A[i+1] = A[s]
    A[s] = temp

    return i+1
def printQuickS( A):
    length = len(A)
    print("--------------------------------------")
    print("%s Elements Array in Quick Sort Algorithm " % length)
    from timeit import default_timer as timer
    start = timer()
    quickSort( A,0,length-1)
    end = timer()
    print( A )
    print("Time : %s " % (end - start))
    print("--------------------------------------")
'''

def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]  # best case for insertion sort
    print("Normal Array For Ten Elements")
    print(A)
    print("--------------------------------------")
    B = [10,9, 8, 7, 6, 5, 4, 3, 2, 1]  # worst case for insertion sort
    C = random.sample(range(0, 10000), 10)
    D = random.sample(range(0, 10000), 100)
    E = random.sample(range(0, 10000), 1000)
    F = random.sample(range(0, 10000), 10000)
    print("Best Case :")
    printIns(A)
    print("Worst Case :")
    printIns(B)
    print("Random Case :")
    printIns(C)
    printIns(D)
    printIns(E)
    printIns(F)

    printMerge(C)
    printMerge(D)
    printMerge(E)
    printMerge(F)

    '''
    printQuickS(C)
    printQuickS(D)
    printQuickS(E)
    printQuickS(F)
    '''
main()

