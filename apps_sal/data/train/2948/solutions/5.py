def split_by_value(k, elements):
    return [x for f in (lambda x: x < k, lambda x: x >= k) for x in elements if f(x)]
