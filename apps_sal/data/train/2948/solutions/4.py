def split_by_value(k, elements):
    return sorted(elements, key=k.__le__)
