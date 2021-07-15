from itertools import zip_longest, chain
def combine_strings(*args):
    return ''.join(chain(*zip_longest(*args, fillvalue = '')))
