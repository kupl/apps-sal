def s1(n): return 1 + 2 ** n + 3 ** n
def s2(n): return 1 + 2 ** n + 4 ** n
def s3(n): return 1 + 2 ** n + 3 ** n + 4 ** n + 5 ** n + 6 ** n
def st(n): return s3(n) - s2(n) - s1(n)
def sf(n): return (st(n + 1) - 5 * st(n) - 4) / 4


def find_mult10_SF(n):
    i = 1
    k = 0
    result = None
    while k < n:
        s = sf(i)
        i = i + 1
        if s % 10 == 0:
            k = k + 1
            result = s
    return result
