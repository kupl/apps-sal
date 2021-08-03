def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        total = 0
        for i in range(m):
            if i % n == 0:
                total += i
        return total
