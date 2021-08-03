def close_compare(a, b, *args):
    if args:
        if abs(a - b) <= args[0]:
            return 0
    if a == b:
        return 0
    return -1 if a - b < 0 else 1
