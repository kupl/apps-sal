class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        newS = ''
        for c in s:
            if c == '(':
                counter += 1
            elif c == ')':
                if counter == 0:
                    continue
                counter -= 1
            newS += c
            
        result = ''
        for c in newS[::-1]:
            if c == '(' and counter > 0:
                counter -= 1
            else:
                result = c + result
        return result
                

