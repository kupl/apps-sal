MOD = int(1000000000.0 + 7)


def mult(a, b):
    rsp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                rsp[i][j] += a[i][k] * b[k][j]
                rsp[i][j] %= MOD
    return rsp


ident = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m = [[1, 1, 0], [1, 0, 1], [1, 0, 0]]
powers = [m]
for _ in range(53):
    p = powers[-1]
    powers.append(mult(p, p))


def pow2(e):
    y = ident
    i = 0
    for p in powers:
        if e & 1 << i:
            y = mult(p, y)
        i += 1
    return y


t = eval(input())
for _ in range(t):
    n = eval(input())
    if n < 3:
        print(0)
        continue
    r = pow(2, n, MOD)
    b = pow2(n - 2)
    r -= 4 * b[0][0] % MOD
    r -= 2 * b[1][0] % MOD
    r -= b[2][0]
    r = (MOD + r) % MOD
    print(r)
