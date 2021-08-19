from itertools import cycle


class VigenereCipher:

    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        return ''.join((self.caesar(ch, key_ch, 1) if ch in self.alphabet else ch for (ch, key_ch) in zip(text, cycle(self.key))))

    def decode(self, text):
        return ''.join((self.caesar(ch, key_ch, -1) if ch in self.alphabet else ch for (ch, key_ch) in zip(text, cycle(self.key))))

    def caesar(self, char, key_char, mode=1):
        (char_position, move) = (self.alphabet.find(char), self.alphabet.find(key_char))
        return self.alphabet[(char_position + mode * move) % len(self.alphabet)]
