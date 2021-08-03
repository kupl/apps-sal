def howmuch(m, n):
    return [['M: %d' % i, 'B: %d' % (i / 7), 'C: %d' % (i / 9)] for i in range(min(m, n), max(m, n) + 1) if i % 7 == 2 and i % 9 == 1]
