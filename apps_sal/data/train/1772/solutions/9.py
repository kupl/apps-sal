class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.alphabet = alphabet
        self.key = key

    def encode(self, text):
        clé = self.key
        while len(clé) < len(text):
            clé += clé
            clé = clé[:len(text)]
        chiffre = ''
        for (i, (v, w)) in enumerate(zip(text, clé)):
            if v in self.alphabet:
                chiffre += self.alphabet[(self.alphabet.index(v) + self.alphabet.index(w)) % len(self.alphabet)]
            else:
                chiffre += v
        return chiffre

    def decode(self, text):
        clé = self.key
        while len(clé) < len(text):
            clé += clé
            clé = clé[:len(text)]
        dechiffre = ''
        for (i, (v, w)) in enumerate(zip(text, clé)):
            if v in self.alphabet:
                dechiffre += self.alphabet[(self.alphabet.index(v) - self.alphabet.index(w)) % len(self.alphabet)]
            else:
                dechiffre += v
        return dechiffre
