def encode(message, key):
    strKey = str(key)
    return [ord(letter) - 96 + int(strKey[index % len(strKey)]) for index, letter in enumerate(message)]
