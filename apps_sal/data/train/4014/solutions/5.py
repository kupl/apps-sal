import itertools
def combine_strings(*args):
    return "".join(("".join(i) for i in itertools.zip_longest(*args,fillvalue="")))
