from string import maketrans as mt, ascii_lowercase as lc, ascii_uppercase as uc


def encryptor(key, message):
    key %= 26
    return message.translate(mt(lc + uc, lc[key:] + lc[:key] + uc[key:] + uc[:key]))
