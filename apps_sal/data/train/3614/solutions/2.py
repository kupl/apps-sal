def interpreter(tape):
    dct, selector, out = {0:0}, 0, ''
    for l in tape:
        if l == '>': selector += 1
        if l == '<': selector -= 1
        if l == '*': out += chr(dct.get(selector,0))
        if selector in dct:
            if l == '+': dct[selector] = (dct[selector] + 1) % 256
            if l == '-': dct[selector] = (dct[selector] - 1) % 256
            if l == '/': dct[selector] = 0
        if l == '!': dct[ max(dct)+1 ] = 0
    return out
