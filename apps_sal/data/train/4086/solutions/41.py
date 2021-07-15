def first_non_consecutive(arr):
    for n in arr:
        if n != arr.index(n)+arr[0]:
            return n
