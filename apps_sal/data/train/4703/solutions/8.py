def bar_triang(*points):
    return [round(sum(x) / 3.0, 4) for x in zip(*points)]
