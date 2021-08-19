from itertools import chain, zip_longest


def de_nico(key, msg):
    columns = [msg[n::len(key)] for n in range(len(key))]
    key = (n for (n, c) in sorted(enumerate(key), key=lambda k: k[1]))
    return ''.join(chain(*zip_longest(*sorted(columns, key=lambda k: next(key)), fillvalue=''))).strip()
