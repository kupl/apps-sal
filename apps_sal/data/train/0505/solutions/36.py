class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        N = len(s)
        if N == 1 and s[0] in ('(',')'):
            return s.replace(s[0],'')
        index = []
        stack = []
        
        for i,c in enumerate(s):
            if c == '(':
                index.append(i)
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    index.append(i)
                    stack.append(c)
                elif stack[-1] == '(':
                    index.pop()
                    stack.pop()
                else:
                    index.append(i)
                    stack.append(c)
            else:
                continue
        res = ''
        #print (index)
        for i in range(N):
            if i not in index:
                res += s[i]
        
        return res
                    
                

