def replace_zero(lst):
    z = [-1] + [i for i, n in enumerate(lst) if not n] + [len(lst)]
    return max((z[i+1]-z[i-1], z[i]) for i in range(1, len(z)-1))[1]

