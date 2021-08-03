def encode(str, key):
    key = key.lower() + key.upper()
    dict = {char: key[i - 1] if i % 2 else key[i + 1] for i, char in enumerate(key)}
    return ''.join(dict.get(char, char) for char in str)


decode = encode
