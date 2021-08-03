def series_sum(n):
    if n == 0:
        return '0.00'
    final = 0
    x = 0
    while n >= 1:
        final += 1 / (1 + x)
        x += 3
        n -= 1
    final = str(final)
    if len(final) < 4:
        final += '0'
    if len(final) > 4:
        if int(final[4]) > 4:
            final = str(float(final) + .01)
    return str(final)[:4]
