def decode(message):
    return ''.join([chr(ord('z') - (ord(x) - ord('a'))) if x != ' ' else ' ' for x in list(message)])
