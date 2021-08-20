keyboard = ['qwertyuiop', 'QWERTYUIOP', 'asdfghjkl', 'ASDFGHJKL', 'zxcvbnm,.', 'ZXCVBNM<>']


def encrypt(text, encryptKey):
    return crypt(text, encryptKey, 1)


def decrypt(text, encryptKey):
    return crypt(text, encryptKey, -1)


def crypt(text, encryptKey, dir):
    encryptKey = str(encryptKey).zfill(3)
    new_keyboard = [row[int(encryptKey[i // 2]) * dir:] + row[:int(encryptKey[i // 2]) * dir] for (i, row) in enumerate(keyboard)]
    return ''.join([char.translate(str.maketrans(' '.join(keyboard), ' '.join(new_keyboard))) for char in text])
