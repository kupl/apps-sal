is_increasing_sequence = lambda a: all(x < y for x, y in zip(a, a[1:]))
almost_increasing_sequence = lambda a: any(is_increasing_sequence(a[:i] + a[i+1:]) for i in range(len(a)))
