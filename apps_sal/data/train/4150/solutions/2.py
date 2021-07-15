def rot13(message):
    import codecs
    return codecs.encode(message, 'rot_13')
