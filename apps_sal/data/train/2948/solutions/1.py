def split_by_value(k, elements):
    return [x for x in elements if x < k] + [x for x in elements if x >= k]
