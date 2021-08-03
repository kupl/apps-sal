from math import sqrt
for _ in range(int(input())):
    N, MOD = int(input()), 1000000007
    print(((N - 1) ** 2) + (N ** 3) % MOD)
