def max_number(n):
    l = []
    n = str(n)
    for i in n:
        l.append(i)
    l.sort(reverse=True)
    return int(''.join(l))
