from statistics import mean


def avg_array(arrs):
    return [mean(arr) for arr in zip(*arrs)]
