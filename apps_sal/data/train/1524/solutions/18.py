M = 1000000007


def expmod_iter(a, b, c):
    x = 1
    while b > 0:
        if b & 1 == 1:
            x = x * a % c
        a = a * a % c
        b >>= 1
    return x % c


t = eval(input())
while t > 0:
    t -= 1
    (n, k) = list(map(int, input().split()))
    if n >= 2 and k <= 1:
        print(0)
    else:
        print(k * expmod_iter(k - 1, n - 1, M) % M)
