import string


def encryptor(key, message):
    transtab = string.maketrans(string.ascii_letters, (string.ascii_lowercase * 2)[key % 26:key % 26 + 26] + (string.ascii_uppercase * 2)[key % 26:key % 26 + 26])
    return message.translate(transtab)
