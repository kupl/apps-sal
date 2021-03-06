k = 72
kk = k // 4
K = 1 << k


def nu(L, sl=-1):
    if sl == -1:
        sl = slice(0, len(L))
    return int(''.join([hex(K + a)[3:] for a in L[sl][::-1]]), 16)


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
    fg = li(st(nuf * nu(iv[1:2 * d + 2])), d, d * 2 + 1)
    for (i, (_fg, _ti)) in enumerate(zip(fg, ti)):
        h[i] = h[i] * (_fg * t[d + i + 1] % P * _ti % P) % P
    fg1 = li(st(nuf * nu(inv[1:2 * d + 2])), d, d * 2 + 1)
    fg2 = li(st(nuf * nu(iv[d + 2:3 * d + 3])), d, d * 2 + 1)
    fg1.pop()
    for (i, (_fg1, _fg2)) in enumerate(zip(fg1, fg2)):
        h[i + d + 1] = _fg1 * _fg2 % P * fa[d + i + 1] % P * fainv[i] % P * t[2 * d + i + 2] % P * ti[d + i + 1] % P
    return h


def create_table(v, start=1):
    s = 1
    X = [start, v + start]
    while s < v:
        X = grow(s, v, X, start)
        s *= 2
    table = [1]
    for x in X:
        table.append(table[-1] * x % P)
    return table


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


def prod(a, b, vv):
    T = create_table(vv, a)
    c = b - a
    s = T[c // vv]
    for i in range(c // vv * vv + a, b):
        s = s * i % P
    return s


def C(a, b):
    if not 0 <= b <= a:
        return 0
    if b * 2 > a:
        b = a - b
    return prod(a - b + 1, a + 1, v) * pow(prod(1, b + 1, v), P - 2, P) % P


(N, M) = map(int, input().split())
s = sum([int(a) for a in input().split()])
print(C(N + M, s + N))
