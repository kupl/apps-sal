def avg_array(arrs):

    return [sum(a) / len(a) for a in list(zip(*arrs))]
