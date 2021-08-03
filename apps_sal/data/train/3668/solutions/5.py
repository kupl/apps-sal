def s1(n): return 1 + 2 ** n + 3 ** n
def s2(n): return 1 + 2 ** n + 4 ** n
def s3(n): return 1 + 2 ** n + 3 ** n + 4 ** n + 5 ** n + 6 ** n
def st(n): return s3(n) - s2(n) - s1(n)
def sf(n): return (st(n + 1) - 5 * st(n) - 4) / 4


mem = []


def find_mult10_SF(n):
    x = mem[-1][0] + 1 if mem else 1
    while len(mem) < n:
        s = sf(x)
        while s % 10 != 0:
            x += 1
            s = sf(x)
        mem.append((x, s))
        x += 1
    return mem[n - 1][1]
