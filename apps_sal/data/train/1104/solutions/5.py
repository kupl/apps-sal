import math
mod = 1000000007
T = int(input())
for _ in range(T):
    (n, m) = list(map(int, input().split()))
    if n == 0:
        print(m * (m - 1) % mod)
    elif m == 1:
        print((n * (n - 1) + n) % mod)
    else:
        val = n - 1 + math.ceil((m - 1) / 2)
        fv = val * (val + 1) % mod
        if (m - 1) % 2 == 0:
            fv = (fv + 2 * (val + 1) - n) % mod
        else:
            fv = (fv + n) % mod
        print(fv % mod)
