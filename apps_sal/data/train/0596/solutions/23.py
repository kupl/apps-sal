t = int(input())
while t:
    (n, k) = map(int, input().split())
    x = k // 2
    if n == 0:
        print(k * (k - 1) % 1000000007)
    elif k % 2 == 0:
        print(((n + x) * (n + x) - x) % 1000000007)
    else:
        print(((n + x) * (n + x) + x) % 1000000007)
    t -= 1
