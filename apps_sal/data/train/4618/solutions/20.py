''' Suma únicamente los valores positivos, los negativos se los salta.
    En caso de que la lista esté vacía, devuelve 0
'''


def positive_sum(arr):
    sum = 0
    if not arr:
        return sum
    for n in arr:
        if(n >= 0):
            sum = sum + n
    return sum
