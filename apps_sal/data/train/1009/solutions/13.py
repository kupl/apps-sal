from math import gcd


def f(cp, cg):
    nonlocal n, arr

    if cp == n and cg == 1:
        return 1
    elif cp == n:
        return 0
    elif cg == 1:
        return 2**(n - cp)
    elif (cp, cg) in d:
        return d[(cp, cg)]
    else:
        temp = f(cp + 1, cg) + f(cp + 1, gcd(arr[cp], cg))
        d[(cp, cg)] = temp
        return temp


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    d = {}
    ans = 0
    for i in range(n):
        ans += f(i + 1, arr[i])
    print(ans)
