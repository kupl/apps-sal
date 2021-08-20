def decode(code, key):
    key = str(key)
    return ''.join([chr(code[i] + 96 - int(key[i % len(key)])) for i in range(0, len(code))])
