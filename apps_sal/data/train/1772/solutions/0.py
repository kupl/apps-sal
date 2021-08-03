from itertools import cycle


class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.key = key.decode('utf-8')
        self.alphabet = alphabet.decode('utf-8')

    def cipher(self, mode, str):
        return ''.join(self.alphabet[(self.alphabet.index(m) +
                                      mode * self.alphabet.index(k)) % len(self.alphabet)]
                       if m in self.alphabet else m for m, k in zip(str.decode('utf-8'),
                                                                    cycle(self.key))).encode('utf-8')

    def encode(self, str): return self.cipher(1, str)
    def decode(self, str): return self.cipher(-1, str)
