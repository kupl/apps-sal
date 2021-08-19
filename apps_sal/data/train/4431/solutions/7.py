def decode(message):
    import string
    ltrs = dict(list(zip(string.ascii_lowercase, string.ascii_lowercase[::-1])))
    return ''.join((ltrs.get(c, ' ') for c in message))
