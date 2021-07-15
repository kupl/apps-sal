from itertools import zip_longest

def transpose_two_strings(lst):
    return "\n".join(f"{a} {b}" for a, b in zip_longest(*lst, fillvalue=" "))
