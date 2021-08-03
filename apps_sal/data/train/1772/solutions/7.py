from itertools import cycle
# cycle => cycle(abc) = abcabcabc


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str) -> None:
        self.key = key
        self.alphabet = alphabet

    def cipher(self, m: int, s: str) -> str:
        r = ''
        for i, j in zip(s, cycle(self.key)):
            if i in self.alphabet:
                r += self.alphabet[(self.alphabet.index(i) + m * self.alphabet.index(j)) % len(self.alphabet)]
            else:
                r += i
        return r

    def encode(self, s: str) -> str:
        return self.cipher(1, s)

    def decode(self, s: str) -> str:
        return self.cipher(-1, s)
