from itertools import accumulate, chain, islice
from operator import mul


def product_sans_n(nums):
    forward = islice(accumulate(chain([1], nums), mul), 0, len(nums), 1)
    backward = list(accumulate(chain([1], reversed(nums)), mul))[-2::-1]
    return list(map(mul, forward, backward))
