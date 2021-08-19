def get_function(a):
    d = [j - i for (i, j) in zip(a, a[1:])]
    return ['Non-linear sequence', lambda v: d[0] * v + a[0]][len(set(d)) == 1]
