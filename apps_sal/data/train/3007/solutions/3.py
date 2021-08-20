from functools import partial
from itertools import accumulate, count, takewhile
from operator import ge


def consecutive_sum(num):
    return sum(((num - start) % step == 0 for (step, start) in enumerate(takewhile(partial(ge, num), accumulate(count(1))), 1)))
