def repeating_fractions(n, d):
    return str((n + 0.0) / d).split('.')[0] + '.' + ''.join([['({})'.format(i), i][len(list(j)) == 1] for (i, j) in __import__('itertools').groupby(str((n + 0.0) / d).split('.')[1])])
