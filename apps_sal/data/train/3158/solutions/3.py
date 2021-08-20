def one_down(txt):
    if isinstance(txt, list) or isinstance(txt, int):
        return 'Input is not a string'
    Decode = list(map(ord, txt))
    txt = ''
    for x in Decode:
        if x < 65 or x > 122:
            txt += chr(x)
        elif x == 65 or x == 97:
            txt += chr(x + 25)
        else:
            txt += chr(x - 1)
    return txt
