from typing import Union


def sum_mul(n: int, m: int) -> Union[int, str]:
    """ Find the sum of all multiples of `n` below `m`. """
    return "INVALID" if any(map(lambda _: _ <= 0, [n, m])) else sum([_ for _ in range(m)][::n])
