class VigenereCipher(object):

    def __init__(self, key: str, alphabet: str):
        self.alphabet = list(alphabet)
        self.key = [alphabet.index(i) for i in key]

    def encode(self, text):
        return ''.join([self.alphabet[(self.alphabet.index(text[i]) + self.key[i % len(self.key)]) % len(self.alphabet)] if text[i] in self.alphabet else text[i] for i in range(len(text))])

    def decode(self, text):
        return ''.join([self.alphabet[(self.alphabet.index(text[i]) - self.key[i % len(self.key)]) % len(self.alphabet)] if text[i] in self.alphabet else text[i] for i in range(len(text))])
