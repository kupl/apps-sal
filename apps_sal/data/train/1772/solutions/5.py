class VigenereCipher(object):
    cipherMap = {}
    invCipherMap = {}
    alphabet = ''
    lenAlphabet = -1
    key = ''
    lenKey = -1

    def __init__(self, key, alphabet):
        self.key = key
        self.lenKey = len(self.key)
        self.alphabet = alphabet
        self.lenAlphabet = len(self.alphabet)
        self.cipherMap = dict(list(enumerate(self.alphabet)))
        self.invCipherMap = {val: key for key, val in list(self.cipherMap.items())}

    def __performVigenereCipher__(self, text, performEncode):
        lenText = len(text)
        encodedText = ''

        for i in range(lenText):
            curChar = text[i]
            keyChar = self.key[i % self.lenKey]

            if curChar in self.alphabet:
                charVal = self.invCipherMap[curChar]
                keyVal = self.invCipherMap[keyChar]

                if performEncode:
                    valEncoded = (charVal + keyVal) % self.lenAlphabet
                else:
                    valEncoded = (charVal - keyVal) % self.lenAlphabet

                encodedChar = self.cipherMap[valEncoded]
            else:
                encodedChar = curChar

            encodedText += encodedChar

        return encodedText

    def encode(self, text):
        performEncode = True
        encodedText = self.__performVigenereCipher__(text, performEncode)
        return encodedText

    def decode(self, text):
        performEncode = False
        decodedText = self.__performVigenereCipher__(text, performEncode)
        return decodedText
