from string import ascii_lowercase as l, ascii_uppercase as u


def encryptor(key, message):

    def process(x, abc):
        return x in abc and abc[(abc.index(x) + key) % 26]
    return ''.join((process(c, l) or process(c, u) or c for c in message))
