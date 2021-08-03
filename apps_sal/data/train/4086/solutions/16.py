def first_non_consecutive(arr):
    b = arr.pop(0)
    for i in arr:
        if b + 1 == i:
            b = i
        else:
            return i
