def sumin(n):

    lst = [i for i in range(1, n + 1)]
    summa = sum(lst)
    delta = summa
    for x in lst:
        delta -= x
        summa += delta
    return summa


def sumax(n):
    lst = [i for i in range(1, n + 1)]
    summa = 0
    delta = sum(lst)
    for x in lst:
        summa += delta
        delta += x

    return summa


def sumsum(n):
    return sumin(n) + sumax(n)
