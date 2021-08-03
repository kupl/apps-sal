TRANS = str.maketrans('Ook', '001', ', !')


def okkOokOo(s):
    return ''.join(chr(int(x, 2)) for x in s.translate(TRANS).split('?'))
