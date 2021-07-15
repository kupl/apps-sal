def howmuch(m, n):
    m, n = sorted([m, n])
    return [
        ['M: {}'.format(x), 'B: {}'.format(x // 7), 'C: {}'.format(x // 9)]
        for x in range(-((m - 37) // -63) * 63 + 37, n + 1, 63)]

