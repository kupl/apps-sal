from operator import itemgetter


def sort_it(list_, n):
    return ', '.join(sorted(list_.split(', '), key=itemgetter(n - 1)))
