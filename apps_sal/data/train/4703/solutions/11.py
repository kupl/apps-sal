def bar_triang(*coords):
    return [round(1.0 * sum(c) / len(coords), 4) for c in zip(*coords)]
