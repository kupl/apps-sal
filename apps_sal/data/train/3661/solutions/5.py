def find_part_max_prod(n):
    if n % 3 == 0:
        return [[3] * (n / 3), 3**(n / 3)]
    if n % 3 == 2:
        return [[3] * (n // 3) + [2], 3**(n // 3) * 2]
    if n == 1:
        return 1
    if n % 3 == 1:
        return [[4] + [3] * (n // 3 - 1), [3] * (n // 3 - 1) + [2, 2], 3**(n // 3 - 1) * 4]
