from itertools import cycle as c, islice as isl


def sumDig_nthTerm(ini, p, n):
    return sum(map(int, str(ini + sum(list(isl(c(p), n - 1))))))
