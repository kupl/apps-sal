def convert(x): return sum(map(int, x))
def GT(x, y): return convert(x) > convert(y)
def LT(x, y): return convert(x) < convert(y)
def EQ(x, y): return convert(x) == convert(y)


def qSort(xs):

    if len(xs) == 0:
        return []

    pivot, *xs = xs

    lower = [x for x in xs if LT(x, pivot)]
    eqs = sorted([x for x in xs if EQ(x, pivot)] + [pivot])
    upper = [x for x in xs if GT(x, pivot)]

    return qSort(lower) + eqs + qSort(upper)


def order_weight(xs):
    return " ".join(qSort(xs.split(" ")))
