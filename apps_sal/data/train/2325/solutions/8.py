import sys

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return list(map(int, sys.stdin.readline().split()))
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


S = ins()
T = ins()
conv = {"A": 1, "B": 2}


def solve():
    cums = [0] * (len(S) + 1)
    cumt = [0] * (len(T) + 1)
    for i, x in enumerate(S):
        c = conv[x]
        cums[i + 1] = (cums[i] + c) % 3
    for i, x in enumerate(T):
        c = conv[x]
        cumt[i + 1] = (cumt[i] + c) % 3

    q = ini()
    for i in range(q):
        a, b, c, d = inm()
        if (cums[b] - cums[a - 1]) % 3 == (cumt[d] - cumt[c - 1]) % 3:
            print("YES")
        else:
            print("NO")


solve()
