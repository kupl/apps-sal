def super_size(n):
    n = str(n)
    n = sorted(n)
    n = ''.join(n)
    return int(n[::-1])
