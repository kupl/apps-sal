def flatten(seq):
    for e in seq:
        if isinstance(e, list):
            yield from flatten(e)
        yield e


def locate(seq, value):
    return any(e == value for e in flatten(seq))
