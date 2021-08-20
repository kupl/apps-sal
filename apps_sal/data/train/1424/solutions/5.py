(n, a) = map(int, input().split())
while a > 0:
    if n % 10 == 0:
        n = n // 10
    else:
        n = n - 1
    a = a - 1
print(n)
