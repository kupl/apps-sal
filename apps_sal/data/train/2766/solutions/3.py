def check_concatenated_sum(num, n):
    m = abs(num)
    return m == sum(map(int, str(m))) * int('1' * n or 0)
