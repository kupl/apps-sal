def divisors(n):
    div = 1
    for i in range(1, n + 1 // 2):
        if n % i == 0:
            div += 1
    return div
