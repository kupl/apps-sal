t = int(input())
for z in range(t):
    n, k = list(map(int, input().split()))
    if n % 2 == 0:
        print(n + (k * n // 2))
    else:
        print(n + ((((n - 1) // 2) + 2) * k))
