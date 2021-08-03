def split_by_value(k, elements):
    return [i for i in elements if i < k] + [i for i in elements if i >= k]
