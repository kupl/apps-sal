table = ''.join(map(chr, range(65, 91))) * 2
table += table.lower()


def encryptor(key, message):
    key %= 26
    result = ''
    for c in message:
        if c in table:
            result += table[table.index(c) + key]
        else:
            result += c
    return result
