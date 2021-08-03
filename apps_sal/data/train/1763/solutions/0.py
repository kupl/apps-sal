from functools import reduce
from operator import mul


def insane_inc_or_dec(x):
    return (reduce(mul, [x + i + i * (i == 10) for i in range(1, 11)]) // 3628800 - 10 * x - 2) % 12345787
