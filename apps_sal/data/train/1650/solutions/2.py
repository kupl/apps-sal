from itertools import combinations_with_replacement


def find_all(sum_dig, digs):
    x = [int(''.join(x)) for x in combinations_with_replacement('123456789', digs) if sum(map(int, x)) == sum_dig]
    return [len(x), min(x), max(x)] if len(x) > 0 else []
