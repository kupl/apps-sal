class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key * 10
        self.alphabet = alphabet * 2
        
    
    def encode(self, text):
        encrypted = ""
        a = 0
        for i in text:
            if i in self.alphabet:
                encrypted += self.alphabet[self.alphabet.index(i) + self.alphabet.index(self.key[a])]
                a += 1
            else:
                encrypted += i
                a += 1
        return encrypted
        
              
    def decode(self, text):
        decrypted = ""
        a = 0
        for i in text:
            if i in self.alphabet:
                decrypted += self.alphabet[self.alphabet.index(i) - self.alphabet.index(self.key[a])]
                a += 1
            else:
                decrypted += i
                a += 1
        return decrypted
