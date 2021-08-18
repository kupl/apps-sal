def sum_mix(arr):

    suma = int(0)
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    for i in arr:
        suma += i
    return suma
