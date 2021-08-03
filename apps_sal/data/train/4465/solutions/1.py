def super_size(n):
    b = list(str(n))
    b.sort(reverse=True)
    return int("".join(b))
