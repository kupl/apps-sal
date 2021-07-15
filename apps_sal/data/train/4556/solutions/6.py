from itertools import groupby

def count_me(data):
    return ''.join(str(len(list(g))) + k for k, g in groupby(data)) if data.isdecimal() else ''
