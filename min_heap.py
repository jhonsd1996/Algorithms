import sys
import math


def parent(i):

    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def min_heapify(arr, i, n):
    l = left(i)
    r = right(i)
    smallest = i
    if l < n and arr[l] < arr[i]:
        smallest = l
    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest, n)

def minimum(a):
    return a[0]


def extract_min(a):

    n = len(a)
    if n < 1:
        return
    mini = a[0]
    a[0] = a[n - 1]
    a.pop(n - 1)
    n -= 1
    min_heapify(a, 0, n)
    return mini


def decrease_key(a, i, key):
    if key > a[i]:
        return

    a[i] = key
    while i > 0 and a[parent(i)] > a[i]:
        a[i], a[parent(i)] = a[parent(i)], a[i]
        i = parent(i)


def insert(a, key):
    s = len(a) + 1
    a.append(math.inf)
    decrease_key(a, s - 1, key)

l = list(map(int, sys.stdin.readline().strip().split()))
arr = []
for i in range(0,len(l)):
    insert(arr, l[i])
for j in range(0,len(arr)):
    print(extract_min(arr))
