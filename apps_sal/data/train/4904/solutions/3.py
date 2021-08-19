def iter_unpack(x):
    if isinstance(x, (tuple, list, set)):
        for item in x:
            yield from iter_unpack(item)
    elif isinstance(x, dict):
        for (key, value) in x.items():
            yield from iter_unpack(key)
            yield from iter_unpack(value)
    else:
        yield x


def unpack(x):
    return list(iter_unpack(x))
