from itertools import groupby
def check_double(s):
    return ''.join([x[0] for x in groupby(s) if len(list(x[1])) % 2 != 0])
def doubles(s):
    out = check_double(s)
    while out != check_double(out): out = check_double(out)
    return out
