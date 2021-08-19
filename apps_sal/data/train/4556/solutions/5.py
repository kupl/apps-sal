def count_me(data):
    if not data.isdigit():
        return ''
    output = ''
    from itertools import groupby
    for (k, v) in groupby(data):
        output += str(len(list(v))) + k
    return output
