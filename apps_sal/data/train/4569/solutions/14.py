def next_item(xs, item):
    return (lambda x: next(x, None) if item in x else None)(iter(xs))
