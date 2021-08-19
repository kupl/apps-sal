def sum_str(a, b):
    return f'{int(a) + int(b)}' if a and b else '0' if not a and (not b) else a if not b else b
