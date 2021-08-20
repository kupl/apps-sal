class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        newS = ''
        for c in s:
            if c == ')':
                if counter > 0:
                    counter -= 1
                    newS += c
            elif c == '(':
                counter += 1
                newS += c
            else:
                newS += c
        ans = ''
        for c in newS[::-1]:
            if c == '(' and counter > 0:
                counter -= 1
            else:
                ans = c + ans
        return ans
