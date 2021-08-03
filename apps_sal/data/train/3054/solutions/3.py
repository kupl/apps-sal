def range_(n):
    if n > 0:
        return range(n + 1)
    else:
        return [-i for i in range(-n + 1)]


def sum_of_n(n):
    return [sum(range_(i)) for i in range_(n)]
