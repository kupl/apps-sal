def super_size(n):
    big = list(str(n))
    big.sort(reverse=True)
    return int(''.join(big))
