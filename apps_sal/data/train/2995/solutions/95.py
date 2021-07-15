def sum_mul(n, m):
    total = 0
    while n > 0 and m > 0:
        for i in range(m):
            if abs(i) % n == 0:
                total += i
        return total

    return 'INVALID'

