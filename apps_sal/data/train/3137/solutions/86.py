from math import ceil, floor


def round_it(n):
    dot_index = str(n).find('.')
    len_int_part = dot_index
    len_dec_part = len(str(n)) - dot_index - 1
    if len_int_part < len_dec_part:
        return ceil(n)
    elif len_int_part > len_dec_part:
        return floor(n)
    else:
        return round(n)
