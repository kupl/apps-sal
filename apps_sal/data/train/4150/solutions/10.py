import codecs


def rot13(message):
    code = codecs.encode(message, 'rot_13')
    return(code)
