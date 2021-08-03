def solve(n):
    a = [1]
    n = list(range(2, n + 1))
    while len(n) > n[0]:
        nn = n[:]
        a.append(n[0])
        n = [i for z, i in enumerate(nn) if z % n[0] != 0 and z != 0]
    a += n
    return sum(a)
