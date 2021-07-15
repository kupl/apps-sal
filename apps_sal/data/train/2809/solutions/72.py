def digitize(n):
    n = str(n)
    n = n[::-1]
    n = ' '.join(n)
    return [int(i) for i in n.split()]
