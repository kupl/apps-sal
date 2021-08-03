import sys
n = int(input())
L = list(map(int, sys.stdin.readline().split()))

z = L.count(0)

if(z == n or z == 0):
    print(0)
    Zeros = [0] * n
    Zeros[n - 1] += 1 - L[n - 1]
    for i in range(n - 2, -1, -1):
        Zeros[i] = Zeros[i + 1]
        if(L[i] == 0):
            Zeros[i] += 1
else:
    Zeros = [0] * n
    Zeros[n - 1] += 1 - L[n - 1]
    for i in range(n - 2, -1, -1):
        Zeros[i] = Zeros[i + 1]
        if(L[i] == 0):
            Zeros[i] += 1

    Ans = 0
    o = 0
    z = 0
    p = L[0]
    if(L[0] == 1):
        o += 1
    for i in range(1, n):
        if(L[i] == p):

            if(p == 1):
                o += 1
        else:
            if(L[i] == 0):
                Ans += Zeros[i] * o
                p = 0
            else:
                o = 1
                p = 1
    print(Ans)
