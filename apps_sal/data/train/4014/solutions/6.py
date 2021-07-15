from itertools import zip_longest

def combine_strings(*args):
    return ''.join(map(''.join, zip_longest(*args, fillvalue='')))
