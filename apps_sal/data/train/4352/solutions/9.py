def encrypt(text, rule):
    retval = ''
    for sss in text:
        retval += chr((ord(sss) + rule) % 256)
    return retval
