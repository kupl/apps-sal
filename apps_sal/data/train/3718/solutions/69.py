def divisors(n):
    count = 1
    for i in range(1, n):
        if n % i == 0:
            count += 1
        else:
            count += 0
    return count
