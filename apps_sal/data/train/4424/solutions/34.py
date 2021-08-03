from itertools import product
from operator import mul, add


def expression_matter(a, b, c):
    if not 1 in [a, b, c]:
        return a * b * c
    return max(
        max(
            op1(a, op2(b, c)),
            op1(op2(a, b), c)
        )
        for op1, op2 in product([mul, add], repeat=2)
    )
