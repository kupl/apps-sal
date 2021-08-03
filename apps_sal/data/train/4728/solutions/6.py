from itertools import zip_longest


def populate_dict(keys, default): return dict(zip_longest(keys, [default], fillvalue=default))
