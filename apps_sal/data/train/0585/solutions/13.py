import math as x


def lfact(n, k):
    fact = []
    max = 0
    for j in range(1, int(k ** 0.5) + 1):
        if k % j == 0:
            if j <= n and j > max:
                max = j
            if k // j <= n and k // j > max:
                max = k // j
    return max


t = int(input())
for j in range(t):
    (n, m) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if n == 1:
        print(0)
    else:
        g = 0
        for i in range(m):
            g = x.gcd(arr[i], g)
        if g > n:
            g = lfact(n, g)
            print(n - g)
        elif g == n:
            print(0)
        else:
            print(n - g)
