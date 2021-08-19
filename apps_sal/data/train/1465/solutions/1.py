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


def circles(u):
    r = 0
    S = [(u, -1, 0)]
    Been = [-1] * n
    Been[u] = 0
    for s in S:
        Visited[s[0]] = 1
        for e in V[s[0]]:
            if e[0] != s[1]:
                if Been[e[0]] == -1:
                    Been[e[0]] = s[2] ^ e[1]
                    S.append((e[0], s[0], s[2] ^ e[1]))
                elif Been[e[0]] != s[2] ^ e[1]:
                    return -1
                else:
                    r += s[0] < e[0]
    return r


T = int(sys.stdin.readline())
for _ in range(T):
    is_bad = False
    empty = 0
    (n, Q) = list(map(int, sys.stdin.readline().split()))
    for _ in range(n - 1):
        sys.stdin.readline()
    paths = []
    V = list(map(list, [[]] * n))
    E = []
    for q in range(Q):
        (u, v, x) = list(map(int, sys.stdin.readline().split()))
        u -= 1
        v -= 1
        if (v, x ^ 1) in V[u]:
            is_bad = True
        elif (v, x) in V[u]:
            empty += 1
        elif u != v:
            E.append((u, v, x))
            V[u].append((v, x))
            V[v].append((u, x))
        elif x == 1:
            is_bad = True
        else:
            empty += 1
        paths.append((u, v, x))
    if is_bad:
        print(0)
    elif n <= 1:
        print(1)
    else:
        Visited = [0] * n
        components = 0
        for i in range(n):
            if Visited[i] == 0:
                components += 1
                c = circles(i)
                if c == -1:
                    is_bad = True
                    break
                empty += c
        if is_bad:
            print(0)
        else:
            print(powc(2, n - 1 - (Q - empty), 10 ** 9 + 7))
