class Solution:

    def toGoatLatin(self, S: str) -> str:
        result = ''
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        aAppend = 'a'
        newWord = ''
        maAppend = ''
        lastC = ''
        for c in S:
            lastC = c
            fullAppend = maAppend + aAppend
            if c == ' ':
                result += newWord + fullAppend + ' '
                aAppend += 'a'
                newWord = ''
                maAppend = ''
                continue
            if maAppend == '' and c in vowel:
                maAppend = 'ma'
                newWord += c
                continue
            if maAppend == '' and (not c in vowel):
                maAppend = c + 'ma'
                continue
            newWord += c
        if lastC != ' ':
            result += newWord + maAppend + aAppend
        return result
