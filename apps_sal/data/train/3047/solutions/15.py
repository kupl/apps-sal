from itertools import groupby


def repeating_fractions(numerator, denominator):
    int_part, fraction_part = str(numerator / denominator).split('.')
    return int_part + '.' + ''.join(f'({key})' if len(list(group)) > 1 else key for key, group in groupby(fraction_part))
