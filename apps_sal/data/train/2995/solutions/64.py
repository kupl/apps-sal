def sum_mul(n, m):
    if n <= 0:
        return 'INVALID'
    if m <= 0:
        return 'INVALID'
    if n == m:
        return 0
    number_multiples = (m - 1) // n
    total = number_multiples * (number_multiples + 1) // 2
    return_value = total * n
    return return_value
