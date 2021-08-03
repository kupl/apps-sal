import math


def zeros(n: int):
    if n < 5:
        return 0
    log_n_5 = int(math.log(n, 5))

    return sum([n // 5**i for i in range(1, log_n_5 + 1)])
