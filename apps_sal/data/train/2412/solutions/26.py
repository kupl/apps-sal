class Char(object):
    def __init__(self, val):
        self.val = val
        self.count = 1
        
class Solution:
    def removeDuplicates(self, S: str) -> str:
        '''
        similar to 1D candy crush
        '''
        if len(S) == 0:
            return S
        
        stack = [Char(S[0])]
        k = 2 #duplicate
        
        n = len(S)
        
        for i in range(1, n):
            if stack and stack[-1].val == S[i]:
                stack[-1].count += 1
                
                if stack[-1].count == k:
                    stack.pop()
            else:
                stack.append(Char(S[i]))
        
        output = ''
        while stack:
            char = stack.pop()
            output = char.val*char.count + output
        
        return output
        


