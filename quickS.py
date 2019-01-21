#!/usr/bin/python
import sys
import random
import time
import timeit
sys.setrecursionlimit(10000)
ctr = 0
def quickSort(A,b,s):
    global ctr
    if b < s:
        ctr += 1
        r = partition(A,b,s)
        ctr += 1
        quickSort(A,b,r-1)
        ctr += 1
        quickSort(A,r+1,s)
        ctr += 1
def partition (A,b,s):
    global ctr
    pivot = A[s]
    ctr += 1
    i = b - 1
    ctr += 1
    for j in range(b,s):
        ctr += 1
        if A[j] <= pivot:
            ctr += 1
            i = i + 1
            ctr += 1
            temp = A[i]
            ctr += 1
            A[i] = A[j]
            ctr += 1
            A[j] = temp
            ctr += 1
    temp = A[i+1]
    ctr += 1
    A[i+1] = A[s]
    ctr += 1
    A[s] = temp
    ctr += 1
    ctr += 1
    return i+1
def printQuickS( A):
    global ctr
    length = len(A)
    print("--------------------------------------")
    print("%s Elements Array in Quick Sort Algorithm " % length)
    from timeit import default_timer as timer
    start = timer()
    quickSort( A,0,length-1)
    end = timer()
    print( A )
    print("Counter : {0} Time : {1}".format(ctr,(end - start)))
    print("--------------------------------------")
def main():
    A = random.sample(range(0, 10000), 10)
    B = random.sample(range(0, 10000), 100)
    C = random.sample(range(0, 10000), 1000)
    D = random.sample(range(0, 10000), 10000)

    print("Normal Array For Ten Elements")
    print(A)
    print("--------------------------------------")

    printQuickS(A)
    printQuickS(B)
    printQuickS(C)
    printQuickS(D)

main()
