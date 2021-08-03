def avg_array(arrs):
    length = len(arrs)
    return [sum(arr) / length for arr in zip(*arrs)]
