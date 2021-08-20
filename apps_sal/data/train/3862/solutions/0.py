def mirror(code, chars='abcdefghijklmnopqrstuvwxyz'):
    return code.lower().translate(str.maketrans(chars, chars[::-1]))
