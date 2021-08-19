lowers = 'abcdefghijklmnopqrstuvwxyz '


def keyword_cipher(msg, keyword):
    key = ''.join(sorted(lowers, key=f'{keyword.lower()}{lowers}'.index))
    return ''.join((key[lowers.index(char)] for char in msg.lower()))
