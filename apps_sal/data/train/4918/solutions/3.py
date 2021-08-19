def convert(n):
    ls = [int(j) if i % 4 <= 1 else -int(j) for (i, j) in enumerate(str(n)[::-1])]
    return [sum(ls[::2]), sum(ls[1::2])]
