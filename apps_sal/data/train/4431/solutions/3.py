def decode(m):
    return m.translate({k: v for (k, v) in zip(range(97, 123), range(122, 96, -1))})
