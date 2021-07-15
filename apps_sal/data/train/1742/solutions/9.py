
import itertools
d = {1:[[1]]}
def combos(n):
    if n not in d:
        d[n] = list(i for i,_ in itertools.groupby(sorted([[n]] + [sorted(j+[i]) for i in range(1, n) for j in combos(n-i)])))
    return d[n]
