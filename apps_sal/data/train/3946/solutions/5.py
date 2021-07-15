from itertools import zip_longest


def interweave(*args):
    return ''.join(''.join(b for b in a if not b.isdigit())
                   for a in zip_longest(*args, fillvalue='')).rstrip()

