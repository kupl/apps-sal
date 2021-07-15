def remove_smallest(x):
    return [x[i] for i in range(len(x)) if i != x.index(min(x))]

