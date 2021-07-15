from itertools import groupby

def string_parse(str_in):
    if not isinstance(str_in, str):
        return "Please enter a valid string"
    str_out= []
    for _, group in groupby(str_in):
        s = ''.join(group)
        str_out.append(s if len(s) < 3 else f'{s[:2]}[{s[2:]}]')
    return ''.join(str_out)
