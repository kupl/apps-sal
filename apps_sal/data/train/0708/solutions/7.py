t = int(input())
while t > 0:
    t -= 1
    n, k = list(map(int, input().split()))
    p = 0
    m = int(1e9 + 7)
    for i in range(1, n + 1):
        l = pow(k, 2 * i - 1, m)
        p += l
        p = p % m
        k = (k * l) % m
    print(p)
