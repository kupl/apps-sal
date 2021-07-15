def encryptor(key, msg):
    r = ''
    for i in msg:
        if i.isalpha():
            base = 65 if i.isupper() else 97
            r += chr(base + (ord(i)+key - base) % 26)
        else:
            r += i
    return r
