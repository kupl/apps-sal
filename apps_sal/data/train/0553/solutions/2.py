def eqSolve(p, a, q, b):
    x = p - q
    y = a - b
    if x != 0:
        z = int(y / x)
        return z
    else:
        return 1


def solve(p, q, r, a, b, c, rs):
    if p == a and q == b and r == c:
        return rs
    elif rs >= 2:
        return 3
    else:
        res = 3
        m = 8
        adds = [a - p, b - q, c - r]
        muls = []
        if p != 0:
            muls.append(a / p)
        if q != 0:
            muls.append(b / q)
        if r != 0:
            muls.append(c / r)
        muls.append(eqSolve(p, a, q, b))
        muls.append(eqSolve(p, a, r, c))
        muls.append(eqSolve(q, b, r, c))
        for n in range(m):
            for add in adds:
                np = p
                nq = q
                nr = r
                if n & 1 > 0:
                    np = np + add
                if n & 2 > 0:
                    nq = nq + add
                if n & 4 > 0:
                    nr = nr + add
                res = min(res, solve(np, nq, nr, a, b, c, rs + 1))
            for mul in muls:
                np = p
                nq = q
                nr = r
                if n & 1 > 0:
                    np = np * mul
                if n & 2 > 0:
                    nq = nq * mul
                if n & 4 > 0:
                    nr = nr * mul
                res = min(res, solve(np, nq, nr, a, b, c, rs + 1))
        return res


t = int(input())
x = 0
for x in range(t):
    p, q, r = map(int, input().split())
    a, b, c = map(int, input().split())
    y = solve(p, q, r, a, b, c, 0)
    print(y)
