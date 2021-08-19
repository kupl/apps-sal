def beasts(h, t):
    return (lambda m: [t - m, m] if m >= 0 and m <= t and (m % 1 == 0) else 'No solutions')((h - t * 2) / 3.0)
