import sys

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: list(map(int, sys.stdin.readline().split()))
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
# debug = lambda *a, **kw: print(*a, **kw, file=sys.stderr)

S = ins()
T = ins()
conv = {"A": 1, "B": 2}


def solve():
    cums = [0] * (len(S) + 1)
    cumt = [0] * (len(T) + 1)
    for i, x in enumerate(S):
        c = conv[x]  # 1 or 2
        cums[i + 1] = (cums[i] + c) % 3
    for i, x in enumerate(T):
        c = conv[x]  # 1 or 2
        cumt[i + 1] = (cumt[i] + c) % 3

    q = ini()
    for i in range(q):
        a, b, c, d = inm()
        if (cums[b] - cums[a - 1]) % 3 == (cumt[d] - cumt[c - 1]) % 3:
            print("YES")
        else:
            print("NO")


solve()

