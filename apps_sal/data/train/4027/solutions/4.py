def flatten(xs, level=1):
    for x in xs:
        if isinstance(x, list):
            yield from flatten(x, level + 1)
        else:
            yield x, level


def sum_nested_numbers(xs):
    return sum(x ** level for x, level in flatten(xs))
