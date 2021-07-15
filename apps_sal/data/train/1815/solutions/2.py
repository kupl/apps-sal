def caesarCipherEncryptor(string, key):
\tnewString = ''
\tfor i in string:
\t\tnewString += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
\treturn newString

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        newString = \"\"
        l = len(S)
        
        for i in range(1, len(shifts), 1):
            shifts[l - 1 - i] += shifts[l - i]
        j = 0
        for i in S:
            newString += caesarCipherEncryptor(i, shifts[j])
            j += 1
            
        return newString
        
