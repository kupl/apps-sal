class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if (len(stack) == 0):
                stack.append(s[i])
            elif (s[i].isupper() and stack[-1].islower() and (stack[-1].upper() == s[i])):
                stack.pop(-1)
            elif (s[i].islower() and stack[-1].isupper() and (stack[-1].lower() == s[i])):
                  stack.pop(-1)
            else:
                stack.append(s[i])
        return ''.join(stack)
    
    

