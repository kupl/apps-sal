from itertools import groupby


def repeating_fractions(numerator, denominator):
    (int_number, fraction) = str(numerator / float(denominator)).split('.')
    group = []
    for (i, j) in groupby(fraction):
        try:
            next(j)
            next(j)
            group.append('({})'.format(i))
        except StopIteration:
            group.append(i)
    return '{}.{}'.format(int_number, ''.join(group))
