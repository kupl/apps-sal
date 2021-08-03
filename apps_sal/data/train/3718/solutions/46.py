def divisors(n):
    counter = 1
    for i in range(1, n):
        if n % i == 0:
            counter += 1
    return counter


divisors(2)
