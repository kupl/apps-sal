def calc(n, b, m):
    if(n == 1):
        return m
    if(n % 2 == 0):
        return m * n / 2 + b + calc(n / 2, b, m * 2)
    else:
        return m * (n + 1) / 2 + b + calc((n - 1) / 2, b, m * 2)


t = int(input())
while (t != 0):
    t = t - 1
    n, b, m = list(map(int, input().split()))
    print(calc(n, b, m))
