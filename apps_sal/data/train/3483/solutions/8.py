def string_parse(s):
    from itertools import groupby
    if not isinstance(s, str):
        return 'Please enter a valid string'
    x = [(i, sum([1 for j in group])) for (i, group) in groupby(s)]
    x = [i[0] * 2 + '[' + i[0] * (i[1] - 2) + ']' if i[1] >= 2 else i[0] for i in x]
    x = ''.join(x)
    x = x.replace('[]', '')
    return x
