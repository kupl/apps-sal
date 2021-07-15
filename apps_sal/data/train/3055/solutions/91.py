def sum_str(a, b):
    if not a or not b:
        return "0" if not a and not b else str(a) if not b else str(b)
    return f'{int(a)+int(b)}'
