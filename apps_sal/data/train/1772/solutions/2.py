from itertools import cycle, islice
from unicodedata import normalize

def chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)] if chunk_size != 1 else lst
    

class VigenereCipher (object):
    def __init__(self, key, alphabet):
        self.charsize = len(key) / len(key.decode('utf-8'))
        seq = chunks(list(islice(cycle(key), len(alphabet))), self.charsize)
        seq = [''.join(s) for s in seq]
        self.ab = chunks(alphabet, self.charsize)
        self.key = [self.ab.index(x) for x in seq]
        
    def caesar(self, c, shift):        
        try:
            return self.ab[(self.ab.index(c) + shift) % len(self.ab)]
        except ValueError:
            return c   
        
    def encode(self, str):
        seq = [self.caesar(c, self.key[index]) for index, c in enumerate(chunks(str, self.charsize))]  
        return ''.join(seq)
            
    def decode(self, str):
        seq = [self.caesar(c, -self.key[index]) for index, c in enumerate(chunks(str, self.charsize))]  
        return ''.join(seq)
        

