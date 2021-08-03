def triangular_range(start, stop):
    startn = int(math.ceil(-0.5 + math.sqrt(0.25 + 2 * start)))
    stopn = int(math.floor(-0.5 + math.sqrt(0.25 + 2 * stop)))
    return dict((n, n * (n + 1) / 2) for n in range(startn, stopn + 1))
