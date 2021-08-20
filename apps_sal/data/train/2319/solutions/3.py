import sys
from sys import stdin
tt = int(stdin.readline())
mod = 998244353
for loop in range(tt):
    (n, k) = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    l = [None] * (n + 1)
    r = [None] * (n + 1)
    use = [True] * (n + 1)
    for i in b:
        use[i] = False
    for i in range(n):
        if i != n - 1:
            l[a[i]] = a[i + 1]
        if i != 0:
            r[a[i]] = a[i - 1]
    ans = 1
    for i in range(k):
        now = 0
        if l[b[i]] != None and use[l[b[i]]]:
            now += 1
        if r[b[i]] != None and use[r[b[i]]]:
            now += 1
        ans *= now
        ans %= mod
        if l[b[i]] != None:
            r[l[b[i]]] = r[b[i]]
        if r[b[i]] != None:
            l[r[b[i]]] = l[b[i]]
    print(ans % mod)
