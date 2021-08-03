from itertools import permutations


def rearranger(k, *args):
    min_d = [10e50, None]
    for p in permutations(args):
        n = int(''.join(str(x) for x in p))
        if n % k == 0:
            if n < min_d[0]:
                min_d = [n, set({', '.join(map(str, p))})]
            elif n == min_d[0]:
                min_d[1].add(', '.join(map(str, p)))
    if min_d[1] is None:
        return 'There is no possible rearrangement'
    return 'Rearrangement: {0} generates: {1} divisible by {2}'.format(' and '.join(min_d[1]), min_d[0], k)
