from string import ascii_lowercase as l, ascii_uppercase as u

def encryptor(key, message):
    process = lambda x, abc: x in abc and abc[(abc.index(x) + key) % 26]
    return ''.join(process(c, l) or process(c, u) or c for c in message)
