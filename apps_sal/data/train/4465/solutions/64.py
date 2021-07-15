def super_size(n):
    x = sorted([int(x) for x in str(n)])[::-1]
    return int(''.join(map(str, x)))
