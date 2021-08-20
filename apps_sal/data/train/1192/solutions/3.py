import math


def solveit(A, n):
    N = n
    G = []
    for i in range(n):
        v = math.gcd(A[i], A[(i + 1) % N])
        if v == 1:
            G.append(1)
        else:
            G.append(0)
    pos = -1
    for i in range(n):
        if G[i] == 1:
            pos = i
            break
    V = []
    ans = [0 for i in range(N - 1)]
    if pos == -1:
        for i in range(N - 1):
            ans[i] = math.ceil(N / (i + 1))
    else:
        c = 0
        for i in range(1, N + 1):
            if G[(pos + i) % N] == 0:
                c = c + 1
            else:
                if c != 0:
                    V.append(c)
                c = 0
        for val in V:
            for i in range(min(val, N - 1)):
                ans[i] = ans[i] + val // (i + 1)
    print(*ans)


for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    solveit(A, n)
