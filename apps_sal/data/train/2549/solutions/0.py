class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.split()
        if len(s) == 1: 
            text = ''.join(s) + ' '*text.count(' ')
            return text
        count = text.count(' ')//(len(s)-1)
        extra = text.count(' ')%(len(s)-1)
        result = ''
        num = 0
        for c in s:
            result += c
            num += 1
            if num <= (len(s)-1):
                result += ' '*count
        qqqqqqqqq = [3]*100000
        if extra != 0:
            result += ' '*extra
        return result
