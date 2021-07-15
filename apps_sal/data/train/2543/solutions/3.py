import string
# string.ascii_letters
# string.ascii_uppercase
# string.ascii_lowercase
# c.isalpha()
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if not S: return ''
        
        stack = []
        deque = collections.deque()
        for i, c in enumerate(S):
            # if c not in string.ascii_letters: #'abcd...'
            if not c.isalpha():
                deque.append((i, c))
            else:
                stack.append(c)

        res = ''
        for i in range(len(S)):
            if deque and i == deque[0][0]:
                res += deque.popleft()[1]
                
            else:
                res += stack.pop()
        return res
    

