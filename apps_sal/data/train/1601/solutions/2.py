def check(n, p, divisor):
    product = 1
    if p > n:
        i = p - n
        j = p - n
        k = 1
        product = i * j
        i = 1
        j = p - n % divisor
        k = j
        product += i * j * k
        i = p - n
        j = 1
        k = p - n % divisor
        product += i * j * k
        print(product)
    elif p <= n and p >= divisor:
        i = 1
        j = p - n % divisor
        k = j
        product = i * j * k
        print(product)
    elif p < divisor:
        greatest = 0
        for m in range(1, p):
            if n % m > greatest:
                greatest = n % m
        i = 1
        j = p - greatest
        k = p - greatest
        product = i * j * k
        print(product)


t = int(input())
while t > 0:
    (n, p) = tuple(map(int, input().split()))
    if n <= 2:
        print(p * p * p)
    elif n % 2 == 0:
        check(n, p, n // 2 + 1)
    else:
        check(n, p, (n + 1) // 2)
    t -= 1
