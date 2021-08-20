def memorysize_conversion(size):
    (x, unit) = size.upper().split()
    (x, (u, *i, _)) = (float(x), unit)
    op = float.__mul__ if i else float.__truediv__
    (p, conv) = ('_KMGT'.index(u), f"{u}{('' if i else 'i')}B")
    return f'{round(op(x, 1.024 ** p), 3)} {conv}'.replace('KB', 'kB')
