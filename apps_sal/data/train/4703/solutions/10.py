def bar_triang(*pts):
    return [round(1.0 * sum(ps) / len(pts), 4) for ps in zip(*pts)]
