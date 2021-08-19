def super_size(n):
    return int(''.join((str(x) for x in sorted([int(a) for a in str(n)], reverse=True))))
