def super_size(n):
    lst = sorted([int(c) for c in str(n)], reverse=True)
    return int(''.join([str(i) for i in lst]))
