pentagonals = set()
generalized_pentagonals = set([0])
square_pentagonals = set()
for i in range(1, 10**6):
    x = (3 * i**2 - i) // 2
    y = (3 * i**2 + i) // 2
    pentagonals.add(x)
    generalized_pentagonals.add(x)
    generalized_pentagonals.add(y)
    if (x**0.5).is_integer():
        square_pentagonals.add(x)


def p_num(n):
    return n in pentagonals


def g_p_num(n):
    return n in generalized_pentagonals


def s_p_num(n):
    return n in square_pentagonals
