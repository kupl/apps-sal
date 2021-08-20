mod = 1000000007
(n, q) = map(int, input().split())
l = n + 1 % mod
r = n + 1 % mod
t = 1 % mod
b = pow(2, n) % mod
e = (pow(2, n + 1) - 2) % mod
for _ in range(q):
    lst = list(map(int, input().split()))
    if len(lst) != 1:
        if lst[1] == 1:
            e = (2 * e + l) % mod
            l = l
            r = r
            t = 2 * t % mod
            b = 2 * b % mod
        if lst[1] == 2:
            e = (2 * e + r) % mod
            l = l
            r = r
            t = 2 * t % mod
            b = 2 * b % mod
        if lst[1] == 3:
            e = (2 * e + t) % mod
            t = b % mod
            l = 2 * l % mod
            r = 2 * r % mod
            b = b % mod
        if lst[1] == 4:
            e = (2 * e + b) % mod
            b = t % mod
            l = 2 * l % mod
            r = 2 * r % mod
            b = b % mod
    else:
        print(e)
