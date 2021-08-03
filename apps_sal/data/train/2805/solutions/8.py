from bisect import *


def genProdFib():
    a, b = 0, 1
    while 1:
        yield a * b, b
        a, b = b, a + b


GEN, PROD = genProdFib(), [(-1, 0)]


def productFib(p):
    def formatOut(pp, b): return [pp // b, b, pp == p]

    if PROD[-1][0] > p:
        return formatOut(*PROD[bisect(PROD, (p, 0))])

    while PROD[-1][0] < p:
        PROD.append(next(GEN))
    return formatOut(*PROD[-1])
