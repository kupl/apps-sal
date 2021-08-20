def first_non_consecutive(arr):
    lena = len(arr)
    b = arr[0]
    for i in arr:
        if b == i:
            b = b + 1
            print('tut')
        else:
            return i
