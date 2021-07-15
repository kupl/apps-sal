s1 = lambda n : 1 + 2 ** n + 3 ** n
s2 = lambda n : 1 + 2 ** n + 4 ** n
s3 = lambda n : 1 + 2 ** n + 3 ** n + 4 ** n + 5 ** n + 6 ** n
st = lambda n : s3(n) - s2(n) - s1(n)
sf = lambda n : (st(n+1) - 5 * st(n) - 4) / 4

mem = []

def find_mult10_SF(n):
    x = mem[-1][0] + 1 if mem else 1
    while len(mem) < n:
        s = sf(x)
        while s % 10 != 0:
            x += 1
            s = sf(x)
        mem.append((x,s))
        x += 1
    return mem[n - 1][1]
