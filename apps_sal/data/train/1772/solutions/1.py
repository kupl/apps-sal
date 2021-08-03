class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')
        self.maps = {c: (self.alphabet[i:] + self.alphabet[:i]) for i, c in enumerate(self.alphabet) if c in self.key}

    def code(self, f, s):
        return ''.join([f(self.maps[self.key[i % len(self.key)]], c) for i, c in enumerate(s.decode('utf-8'))]).encode('utf-8')

    def encode(self, s):
        return self.code(lambda l, c: l[self.alphabet.index(c)] if c in self.alphabet else c, s)

    def decode(self, s):
        return self.code(lambda l, c: self.alphabet[l.index(c)] if c in self.alphabet else c, s)
