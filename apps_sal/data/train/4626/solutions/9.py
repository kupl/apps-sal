def decode(string_):
    if not isinstance(string_, str):
        return 'Input is not a string'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    print(string_)
    out = ''
    for x in string_:
        if x.lower() in alph:
            n = 25 - alph.index(x.lower())
            if x.isupper():
                out += alph[n].upper()
            else:
                out += alph[n]
        else:
            out += x
    return out
