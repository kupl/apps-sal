from functools import lru_cache
from itertools import combinations


@lru_cache(5000)
def get_26_power(i):
    return 26**i


def solve(s):
    greater_letters = list(map(lambda x: 90 - ord(x), s))
    tmp = 1 + sum(greater*get_26_power(i) for i, greater in enumerate(greater_letters[1:]))
    sum_value = 0
    for value in greater_letters:
        sum_value += tmp*value
        tmp = (tmp+25)//26
    return sum_value % 1000000007
