from itertools import chain


def generate_pairs(n):
    return sorted(list(chain.from_iterable([[[a, b] for a in range(b + 1)] for b in range(n + 1)])))
