def deep_count(a):
    return len(a) + sum((deep_count(e) for e in a if isinstance(e, list)))
