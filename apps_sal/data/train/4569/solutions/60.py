def next_item(r, v):
    ix = iter(r)
    try:
        while next(ix) != v:
            continue
        return next(ix)
    except StopIteration:
        return None
