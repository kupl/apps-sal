def two_highest(arg):
    return sorted(list(set(arg)), reverse=True)[:2] if isinstance(arg, list) else False
