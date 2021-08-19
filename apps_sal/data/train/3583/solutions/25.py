def binary_array_to_number(arr):
    arr = arr[::-1]
    sumador = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            sumador += 2 ** i
        else:
            continue
    return sumador
