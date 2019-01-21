#!/usr/bin/python
import sys
import random
import time
import timeit
sys.setrecursionlimit(10000)
ctrM = 0
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


def main():
    A = random.sample(range(0, 10000), 10)
    B = random.sample(range(0, 10000), 100)
    C = random.sample(range(0, 10000), 1000)
    D = random.sample(range(0, 10000), 10000)

    print("Normal Array For Ten Elements")
    print(A)
    print("--------------------------------------")
    printMerge(A)
    printMerge(B)
    printMerge(C)
    printMerge(D)

main()
