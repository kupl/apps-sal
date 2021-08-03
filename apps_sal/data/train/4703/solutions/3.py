def bar_triang(*args):
    return [round(sum(a) / 3.0, 4) for a in zip(*args)]
