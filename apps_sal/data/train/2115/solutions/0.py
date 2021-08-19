import math


def Search(L, aa, x):
    a = aa
    b = len(L)
    while b - a > 1:
        i = (b + a) // 2
        if L[i] > x:
            b = i
        elif L[i] < x:
            a = i
        else:
            return i + 1 - aa - 1
    return b - aa - 1


(n, d) = list(map(int, input().split()))
P = list(map(int, input().split()))
ans = 0
for i in range(n):
    x = Search(P, i, P[i] + d)
    if x > 1:
        ans += x * (x - 1) // 2
print(ans)
