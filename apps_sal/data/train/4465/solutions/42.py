def super_size(n):
    a = list(str(n))
    a.sort(reverse=True)
    n = ''.join(a)
    n = int(n)
    return n
