def find(n):
    m = []
    i = 1
    while i <= n:
        if i % 3 == 0 or i % 5 == 0:
            m.append(i)
        i += 1
    x = sum(m)
    return x
