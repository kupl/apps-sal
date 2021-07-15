def encode(message, key, shift): return cipher(message, key, shift, 1)

def decode(message, key, shift): return cipher(message, key, -shift, 0)

def cipher(message, key, shift, mode):
    key = tuple(dict.fromkeys(key.lower() + 'abcdefghijklmnopqrstuvwxyz'))
    res = ''
    for char in message:
        if char in key:
            i = key.index(char)
            char = key[(i + shift) % 26]
            shift = i + 1 if mode else -key.index(char) - 1
        res += char
    return res
