
def sum_of_minimums(numbers):
    suma = 0
    for arr in numbers:
        suma += min(arr)
    return suma
