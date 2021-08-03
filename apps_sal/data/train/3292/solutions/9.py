def calc(x):
    n1 = "".join([str(ord(c)) for c in x])
    n2 = n1.replace('7', '1')
    return sum(map(int, n1)) - sum(map(int, n2))
