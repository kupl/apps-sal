from collections import Counter
from math import factorial


def count_perms(matrix):
    (m, n) = (len(matrix), len(matrix[0]))
    c = Counter([x for row in matrix for x in row])
    factors = []
    for (x, count) in c.most_common():
        if count > 1:
            factors.append(factorial(count))
    return factorial(m * n) / reduce(lambda a, b: a * b, factors, 1)
