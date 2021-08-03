from string import ascii_lowercase as alphabet


def mirror(code, switches=alphabet):
    key = str.maketrans(switches, switches[::-1])
    return code.lower().translate(key)
