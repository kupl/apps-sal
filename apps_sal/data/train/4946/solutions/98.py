def house_numbers_sum(inp):
    suma = 0
    for n in inp:
        if n == 0:
            break
        suma += n
    return suma
