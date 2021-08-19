def super_size(n):
    b = sorted([int(x) for x in str(n)], reverse=True)
    return int(''.join(map(str, b)))
