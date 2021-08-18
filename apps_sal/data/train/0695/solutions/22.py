from random import randint

f = input


def din(st):
    return bin(st)[2:].zfill(10)


def func(x, y, n):
    z0 = x ^ 0 < y ^ 0
    unmatch = 1
    while z0 == (x ^ unmatch < y ^ unmatch) and unmatch < n + 1:
        unmatch *= 2
    ans = ((n + 1) // (unmatch * 2)) * unmatch
    ans += min(unmatch, (n + 1) - (ans * 2))
    return (ans if z0 else ((n + 1) - ans))


for _ in range(int(f())):
    x, y, n = list(map(int, f().split()))
    print(func(x, y, n))
