"""input
2
3 2 3
1 2 3
3 3 3 
1 2 3
"""
mod = 10 ** 9 + 7
for _ in range(int(input())):
    (n, x, m) = map(int, input().split())
    a = [int(i) for i in input().split()]
    ans = a[x - 1] % mod
    f = 1
    for i in range(1, x):
        f = f * (m - 1 + i)
        f = f // i
        f = f % mod
        ans += a[x - 1 - i] * f % mod
    print(ans % mod)
