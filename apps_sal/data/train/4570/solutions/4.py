def clean_string(string):
    out = ''
    for x in string:
        if x != '
        out += x
        else:
            out = out[:-1]
    return out
