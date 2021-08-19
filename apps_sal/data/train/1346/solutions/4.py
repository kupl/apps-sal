from sys import stdin, stdout
T = int(input().strip())
mod = 10 ** 9 + 7
for _ in range(T):
    (N, W) = map(int, input().strip().split())
    if W > 8 or W < -9:
        print(0)
    else:
        if W >= 0:
            res = (9 - W) * (10 ** (N - 2) % mod)
        else:
            res = (W + 10) * (10 ** (N - 2) % mod)
        print(res % mod)
