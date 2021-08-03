def howmuch(m, n):
    return [['M: {}'.format(i), 'B: {}'.format(int((i - 2) / 7)), 'C: {}'.format(int((i - 1) / 9))] for i in [i for i in range(min(m, n), max(m + 1, n + 1)) if i % 9 == 1 and i % 7 == 2]]
