from itertools import islice, count


def pre_fizz(n):
    return list(islice(count(1), n))
