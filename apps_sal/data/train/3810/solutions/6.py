import numpy


def greatest_product(n):
    lst = []
    for a in range(0, len(n) - 4):
        lst.append(numpy.prod(list(map(int, list(n[a:a + 5])))))
    return max(lst)
