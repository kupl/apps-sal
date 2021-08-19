import codecs


def rot13(message):
    # your code here
    code = codecs.encode(message, 'rot_13')
    return(code)
