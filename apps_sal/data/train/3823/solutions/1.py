def deep_count(a):
    return sum(1 + (deep_count(x) if isinstance(x, list) else 0) for x in a)
