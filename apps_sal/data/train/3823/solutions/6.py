def deep_count(a):
    return len(a) + sum(deep_count(b) for b in a if isinstance(b, list))
