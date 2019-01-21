#!/usr/bin/python
import sys
import random
import time
import timeit
sys.setrecursionlimit(10000)
ctrI = 0
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


def main():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]  # best case for insertion sort
    B = [10,9, 8, 7, 6, 5, 4, 3, 2, 1]  # worst case for insertion sort
    C = random.sample(range(0, 10000), 10)
    D = random.sample(range(0, 10000), 100)
    E = random.sample(range(0, 10000), 1000)
    F = random.sample(range(0, 10000), 10000)
    print("Normal Array For Ten Elements")
    print(C)
    print("--------------------------------------")
    print("Best Case :")
    printIns(A)
    print("Worst Case :")
    printIns(B)
    print("Random Case :")
    printIns(C)
    printIns(D)
    printIns(E)
    printIns(F)

main()

