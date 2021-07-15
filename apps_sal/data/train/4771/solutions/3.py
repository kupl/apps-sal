def encryptor(key, message):
    #Program me!
    key  = key % 26
    result = ''
    for c in message:
        if c >= 'A' and c <= 'Z':
            result += chr(((ord(c) - ord('A')) + key) % 26 + ord('A'))
        elif c >= 'a' and c <= 'z':
            result += chr(((ord(c) - ord('a')) + key) % 26 + ord('a'))
        else:
            result += c
    return result
