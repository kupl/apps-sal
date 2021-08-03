from operator import itemgetter


def sort_it(s, n):
    return ', '.join(sorted(s.split(', '), key=itemgetter(n - 1)))
