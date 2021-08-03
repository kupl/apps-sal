from numpy import mean


def bar_triang(*points):
    return [round(mean(dim), 4) for dim in zip(*points)]
