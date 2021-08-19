def encryptor(key, message):
    table = ''.join(map(chr, list(range(97, 123)))) * 2 + ''.join(map(chr, list(range(65, 91)))) * 2
    return ''.join([table[table.index(c) + key % 26] if c in table else c for c in message])
