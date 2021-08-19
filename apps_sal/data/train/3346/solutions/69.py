def isprime(m):
    if m <= 1:
        return False
    if m <= 3:
        return True
    if m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i * i <= m:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i = i + 6
    return True


def gap(g, m, n):
    hold = None
    for i in range(m, n - 1):
        if isprime(i):
            if hold:
                if i - hold == g:
                    return [hold, i]
            hold = i
    return None
