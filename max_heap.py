import sys
import math


def parent(i):

    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def max_heapify(arr, n, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def maximum(a):
    return a[0]


def extract_max(a):

    n = len(a)
    maxi = a[0]
    a[0] = a[n - 1]
    a.pop(n - 1)
    n -= 1
    max_heapify(a, n, 0)
    return maxi


def increase_key(a, i, key):
    a[i] = key
    while i > 0 and a[parent(i)] < a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


def insert(a, key):
    s = len(a) + 1
    a.append(-math.inf)
    increase_key(a, s - 1, key)

l = list(map(int, sys.stdin.readline().strip().split()))
arr = []
for i in range(0,len(l)):
    insert(arr,l[i])
for j in range(0,len(arr)):
    print(extract_max(arr))
