import itertools


def strings_crossover(arr, result):
    lista = list(itertools.combinations(arr, 2))
    crossovers = 0
    for element in lista:
        flag = True
        for (i, e) in enumerate(result):
            if element[0][i] != e and element[1][i] != e:
                flag = False
        if flag:
            crossovers += 1
    return crossovers
