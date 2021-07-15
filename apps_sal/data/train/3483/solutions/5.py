from itertools import groupby

def string_parse(string):
    if isinstance(string,str):
        gs = groupby(string)
        f = lambda s : s if len(s) < 3 else s[:2] + '[' + s[2:] + ']'
        return ''.join([ f(''.join(list(g))) for _, g in groupby(string)])
    else:
        return 'Please enter a valid string'


