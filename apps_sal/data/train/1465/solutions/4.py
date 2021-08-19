import sys


def powc(x, n, m):
    res = 1
    xx = x
    while n:
        if n & 1:
            res = res * xx % m
        xx = xx * xx % m
        n >>= 1
    return res


def findPath(u, v, x):
    S = [(u, v, x)]
    for s in S:
        if s[0] == v:
            return s[2]
        for e in V[s[0]]:
            if e[0] != s[1]:
                S.append((e[0], s[0], s[2] ^ e[1]))
    return None


T = int(sys.stdin.readline())
for _ in range(T):
    is_bad = False
    empty = 0
    (n, Q) = list(map(int, sys.stdin.readline().split(' ')))
    for _ in range(n - 1):
        sys.stdin.readline()
    paths = []
    V = list(map(list, [[]] * n))
    E = []
    for q in range(Q):
        (u, v, x) = list(map(int, sys.stdin.readline().split(' ')))
        u -= 1
        v -= 1
        if (v, x ^ 1) in V[u]:
            is_bad = True
        elif (v, x) in V[u]:
            empty += 1
        else:
            E.append((u, v, x))
            V[u].append((v, x))
            V[v].append((u, x))
        paths.append((u, v, x))
    if is_bad:
        print(0)
    else:
        while E:
            e = E.pop()
            x = findPath(e[0], e[1], e[2])
            V[e[0]].remove((e[1], e[2]))
            V[e[1]].remove((e[0], e[2]))
            if x == 1:
                is_bad = True
                break
            if x == 0:
                empty += 1
        if is_bad:
            print(0)
        else:
            print(powc(2, n - 1 - (Q - empty), 10 ** 9 + 7))
