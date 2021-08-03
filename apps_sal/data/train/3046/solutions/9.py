thue_morse = m = lambda n, t='0': n > len(t) and m(n, t + t.translate({48: 49, 49: 48})) or t[:n]
