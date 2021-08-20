from functools import reduce
from operator import mul


def maximum_product_of_parts(n):
    s = str(n)
    return max((reduce(mul, map(int, (s[:i], s[i:j], s[j:]))) for i in range(1, len(s) - 1) for j in range(i + 1, len(s))))
