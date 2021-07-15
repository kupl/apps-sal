def super_size(n):
    b = list(str(n))
    b.sort()
    r = ''
    for i in b[::-1]:
        r += i
    return int(r)

