def fisHex(name):
    return eval('^'.join(['0x' + c for c in name.lower() if c in 'abcdef'])) if name else 0
