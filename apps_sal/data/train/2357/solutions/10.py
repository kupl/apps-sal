k = 72
kk = k // 4
K = 1 << k


def nu(L):
    return int(''.join([hex(K + a)[3:] for a in L[::-1]]), 16)


def st(n):
    return hex(n)[2:]


def li(s, l, r):
    return [int(a, 16) % P if len(a) else 0 for a in [s[-(i + 1) * kk:-i * kk] for i in range(l, r)]]


def grow(d, v, h, start):
    h += [0] * d
    f = [(-1 if (i + d) % 2 else 1) * fainv[i] * fainv[d - i] % P * h[i] % P for i in range(d + 1)]
    nuf = nu(f)
    a = d * inv[v] % P
    t = [1] * (3 * d + 3)
    for i in range(1, 3 * d + 3):
        t[i] = t[i - 1] * (a - d + i - 1) % P
    ti = [1] * (3 * d + 3)
    ti[-1] = pow(t[-1], P - 2, P)
    for i in range(1, 3 * d + 3)[::-1]:
        ti[i - 1] = ti[i] * (a - d + i - 1) % P
    iv = [1] * (3 * d + 3)
    for i in range(1, 3 * d + 3):
        iv[i] = ti[i] * t[i - 1] % P
    g = iv[1:2 * d + 2]
    fg = li(st(nuf * nu(g)), d, d * 2 + 1)
    for i in range(d + 1):
        h[i] = h[i] * (fg[i] * t[d + i + 1] % P * ti[i] % P) % P
    g = inv[1:2 * d + 2]
    fg = li(st(nuf * nu(g)), d, d * 2 + 1)
    for i in range(d):
        h[i + d + 1] = fg[i] * fa[d + i + 1] % P * fainv[i] % P
    g = iv[d + 2:3 * d + 3]
    fg = li(st(nuf * nu(g)), d, d * 2 + 1)
    for i in range(d):
        h[i + d + 1] = h[i + d + 1] * (fg[i] * t[2 * d + i + 2] % P * ti[d + i + 1] % P) % P
    return h


def create_table(v, start):
    s = 1
    X = [start, v + start]
    while s < v:
        X = grow(s, v, X, start)
        s *= 2
    table = [1]
    for x in X:
        table.append(table[-1] * x % P)
    return table


def fact(i, table):
    a = table[i // v]
    for j in range(i // v * v + 1, i + 1):
        a = a * j % P
    return a


P = 10 ** 9 + 7
nn = 4000000
v = 1 << (nn.bit_length() + 1) // 2
fa = [1] * (2 * v + 2)
fainv = [1] * (2 * v + 2)
for i in range(2 * v + 1):
    fa[i + 1] = fa[i] * (i + 1) % P
fainv[-1] = pow(fa[-1], P - 2, P)
for i in range(2 * v + 1)[::-1]:
    fainv[i] = fainv[i + 1] * (i + 1) % P
inv = [0] * (2 * v + 2)
for i in range(1, 2 * v + 2):
    inv[i] = fainv[i] * fa[i - 1] % P


def prod(a, b, v):
    T = create_table(v, a)
    c = b - a
    s = T[c // v]
    if c > 10:
        vv = 1 << (c.bit_length() + 1) // 2
        return s * prod(c // v * v + a, b, vv) % P
    for i in range(c // v * v + a, b):
        s = s * i % P
    return s


def C(a, b):
    if b * 2 > a:
        b = a - b
    return prod(a - b + 1, a + 1, v) * pow(prod(1, b + 1, v), P - 2, P) % P


if 1:
    (N, M) = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    s = sum(A)
    print(C(N + M, s + N) if M >= s else 0)
