import math
MOD = 1000000007


def fast_exp(base, exp):
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = res * base % MOD
        base = base * base % MOD
        exp /= 2
    return res


for t in range(int(input())):
    pro = 1
    (a, b) = list(map(int, input().split()))
    pro *= b
    pro *= fast_exp(b - 1, a - 1)
    print(pro % MOD)
