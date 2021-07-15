class Solution:
     def countAndSay(self, n):
       if n < 1:
           raise ValueError('Input should be greater than or equal to 1')
       elif n == 1:
           return '1'
       currentCharacter = ''
       currentCharacterCount = 0
       result = list()
       for character in list(self.countAndSay(n-1)):
           if character != currentCharacter:
               if currentCharacter != '':
                   result.extend([str(currentCharacterCount), currentCharacter])
               currentCharacter = character
               currentCharacterCount = 1
           else:
               currentCharacterCount += 1
       result.extend([str(currentCharacterCount), currentCharacter])
       return ''.join(result)

