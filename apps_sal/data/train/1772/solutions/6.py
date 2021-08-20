class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key

    def encode(self, text):
        mx = []
        for i in range(len(text)):
            try:
                shift = self.alphabet.index(self.key[i % len(self.key)])
                start = self.alphabet.index(text[i])
                mx.append(self.alphabet[(start + shift) % len(self.alphabet)])
            except:
                mx.append(text[i])
        return ''.join(mx)

    def decode(self, text):
        mx = []
        for i in range(len(text)):
            try:
                shift = self.alphabet.index(self.key[i % len(self.key)])
                start = self.alphabet.index(text[i])
                mx.append(self.alphabet[(start - shift) % len(self.alphabet)])
            except:
                mx.append(text[i])
        return ''.join(mx)
