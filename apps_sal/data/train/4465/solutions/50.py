def super_size(n):
    return int(''.join(sorted([digit for digit in str(n)])[::-1]))
