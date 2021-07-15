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
        self.cipherMap = dict(list(enumerate(self.alphabet)))    #slick way learned @ stackExchange :)    
        self.invCipherMap = {val: key for key, val in list(self.cipherMap.items())}   #invert the cipher map
    #-----end constructor



    #helper function to perform the cipher. Note, if a char (in the provided text) is not
    # in the provided alphabet, we are to leave it be; otherwise, based on the alphabet 
    # and the key, we are to encode the character using the Vigenere Cipher    
    def __performVigenereCipher__(self, text, performEncode):
        lenText = len(text)
        encodedText = ''

        for i in range(lenText):
            curChar = text[i]
            keyChar = self.key[i%self.lenKey]

            if curChar in self.alphabet:        #Scenario: Perform Vigenere Cipher
                charVal = self.invCipherMap[curChar]
                keyVal  = self.invCipherMap[keyChar]

                if performEncode:
                    valEncoded = (charVal + keyVal)%self.lenAlphabet
                else:
                    valEncoded = (charVal - keyVal)%self.lenAlphabet

                encodedChar = self.cipherMap[valEncoded] 
            else:   #Scienario: The char is not in the alphabet; leave it be
                encodedChar = curChar
            
            encodedText += encodedChar
        #---end for loop

        return encodedText
    #-----end function

    def encode(self, text):
        performEncode = True
        encodedText = self.__performVigenereCipher__(text, performEncode)        
        return encodedText
    #-----end function encode    
    
    def decode(self, text):
        performEncode = False
        decodedText = self.__performVigenereCipher__(text, performEncode)
        return decodedText 
    #-----end function decode

#-----end class

