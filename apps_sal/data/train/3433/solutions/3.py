import itertools


def replace_zero(arr):
    xs = list(itertools.chain.from_iterable(([length if key else 0] * length for (key, grp) in itertools.groupby(arr) for (_, length) in [(key, sum((1 for _ in grp)))])))
    return max(((0, i) if x else (1 + (xs[i - 1] if i > 0 else 0) + (xs[i + 1] if i < len(xs) - 1 else 0), i) for (i, x) in enumerate(xs)))[1]
