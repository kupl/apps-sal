from math import ceil, floor


def round_it(n):
    case = 2 * str(n).index('.') - len(str(n)) + 1  # len(left) - len(right) = idx - (len(s) - (idx + 1))
    return (round, ceil, floor)[(case < 0) - (case > 0)](n)
