def super_size(n):
    n = str(n)
    a = n[:]
    b = []
    for elem in a:
        b += elem
    b.sort()
    b.reverse()
    s = ""
    s = s.join(b)
    m = int(s)

    return m
