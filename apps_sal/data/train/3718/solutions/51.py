def divisors(n):
    div = 1
    for i in range(1, n):
        if n % i == 0:
            div += 1
    return div
