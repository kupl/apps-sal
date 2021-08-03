def avg_array(arrs):
    return [sum(a) / len(a) for a in zip(*arrs)]
