from itertools import starmap, product
from operator import add, mul


def expression_matter(a: int, b: int, c: int):
    return max(starmap(lambda f, g: max(f(a, g(b, c)), g(f(a, b), c)), product((add, mul), repeat=2)))
