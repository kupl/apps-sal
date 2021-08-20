from functools import reduce


def expression_matter(a, b, c):
    return reduce(lambda accum, next: accum * next if accum * next > accum + next else accum + next, [a, b, c] if c > a else [c, b, a])
