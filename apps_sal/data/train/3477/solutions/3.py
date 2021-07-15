def sort_string(st, order):
    return ''.join(sorted(list(st), key=lambda e: list(order).index(e) if e in order else len(order)))
