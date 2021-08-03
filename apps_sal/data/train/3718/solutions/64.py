def divisors(n):
    count = 0
    for i in range(n + 1):
        if i == 0:
            continue
        s = n / i
        if s.is_integer():
            count += 1
    return count
