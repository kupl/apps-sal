def divisors(n):
    count = 0
    for x in range(n):
        if n % (x + 1) == 0:
            count += 1
    return count
