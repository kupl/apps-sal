def sum_mul(n, m):
    if n < 1 or m < 1:
        return "INVALID"
    multiples_sum = 0
    for num in range(n, m, n):
        multiples_sum += num
    return multiples_sum
