from math import e, factorial


def gta(limit, *nums):
    iternums, l, i, base = [(int(d) for d in str(n)) for n in nums], len(nums), 0, []
    while len(base) < limit:
        d, i = next(iternums[i % l], None), i + 1
        if d is not None and d not in base:
            base.append(d)
    return (int(e * factorial(limit)) * (limit - 1) + 1) * sum(base) // limit
