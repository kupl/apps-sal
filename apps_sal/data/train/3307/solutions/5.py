def fat_fingers(string):
    if string is None:
        return None
    tokens = string.replace('a', 'A').split(sep='A')
    for i, token in enumerate(tokens):
        if i % 2 == 0:
            continue  # CapsLock presses cancel each other out
        tokens[i] = token.swapcase()
    return ''.join(tokens)
