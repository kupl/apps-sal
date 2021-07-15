alphabet = dict(list(zip(__import__('string').ascii_uppercase, '@8(D3F6#!JK1MN0PQR$7UVWXY2')))


def to_leet_speak(str_):
    return ''.join(alphabet.get(x, x) for x in str_)

