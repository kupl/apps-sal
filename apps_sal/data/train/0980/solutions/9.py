def function(n, m, b):
    if n == 1:
        return m
    if n % 2 == 0:
        return n * m / 2 + b + function(n / 2, 2 * m, b)
    else:
        return (n + 1) * m / 2 + b + function((n - 1) / 2, 2 * m, b)


t = int(input())
while (t > 0):
    t = t - 1
    n, b, m = list(map(int, input().split()))
    print(function(n, m, b))
