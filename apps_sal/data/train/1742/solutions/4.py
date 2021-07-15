import itertools
def combos(n):
    return [[1]] if n == 1 else list(i for i,_ in itertools.groupby(sorted([[n]] + [sorted(j+[i]) for i in range(1, n) for j in combos(n-i)])))
