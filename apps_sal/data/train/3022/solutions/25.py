def two_highest(a):
    return sorted(set(a), reverse=True)[:2] if isinstance(a, list) else False
