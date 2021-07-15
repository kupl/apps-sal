def max_number(n):
    n = list(str(n))
    n.sort()
    n.reverse()
    a = []
    for i in n:
        a.append(str(i))
    return int(''.join(a))
