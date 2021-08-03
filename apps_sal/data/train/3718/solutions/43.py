def divisors(n):
    num = list(range(1, n + 1))
    count = 0
    for i in num:
        if n % i == 0:
            count += 1
    return count
