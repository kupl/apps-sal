def sum_of_minimums(argumento):
    suma_min = []

    while argumento != []:
        var = argumento.pop(0)
        minvar = min(var)
        suma_min.append(minvar)

    suma = sum(suma_min)

    return suma
