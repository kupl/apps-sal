def potencia(ls):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    if len(ls) == 0:
        return [[]]
    r = potencia(ls[:-1])
    return r + [s + [ls[-1]] for s in r]


def combina(k, ls):
    """Calcula y devuelve el conjunto potencia del 
       conjunto c.
    """
    return [s for s in potencia(ls) if len(s) == k]


def choose_best_sum(t, k, ls):
    sum = 0
    res = 0
    index = 0
    list = combina(k, ls)
    for m, i in enumerate(list):
        sum = 0
        if len(i) == k:
            for j in i:
                sum += j
        if sum <= t:
            if res < sum:
                res = sum
                index = m

    print(res)
    if res > 0:
        return(res)
    return None
