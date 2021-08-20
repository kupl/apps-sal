def unique_in_order(iterable):
    return [ch for (i, ch) in enumerate(iterable) if i == 0 or ch != iterable[i - 1]]
