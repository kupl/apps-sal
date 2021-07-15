def sum_mix(arr):
    suma = 0
    for i in arr:
        if type(i) == int:
            suma += i
        else:
            suma += int(i)
    return suma
