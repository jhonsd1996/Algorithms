def insertion_sort(arr):

    for j in range(1, len(arr)):
        key = arr[j]

        i = j

        while i > 0 and arr[i - 1] > key:
            arr[i] = arr[i - 1]
            i = i - 1
        arr[i] = key

array = [5, 4, 3, 2, 90, 23]
insertion_sort(array)
print(array)
