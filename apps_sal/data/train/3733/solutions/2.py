from itertools import count, islice


def arithmetic_sequence_elements(a, r, n):
    return ', '.join([str(x) for x in islice(count(a, r), n)])
