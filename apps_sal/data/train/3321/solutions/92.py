def evil(n):

    a = bin(n)
    b = list("".join(a[2:]))
    c = sum([int(i) for i in b])

    if c % 2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"
