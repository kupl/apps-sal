def reverse_it(data):
    t = type(data)
    return t(''.join(reversed(str(data)))) if t in [str, int, float] else data
