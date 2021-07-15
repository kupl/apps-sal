def find(r):
    x = ''.join(['1' if i in r else '0' for i in range(9, -1, -1)])
    return int(x, 2)
