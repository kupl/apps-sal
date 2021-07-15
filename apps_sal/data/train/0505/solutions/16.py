class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        l = list(s)
        stack = []
        i = 0
        while i < len(l):
            if l[i] == '(':
                stack.append(i)
            elif l[i] == ')':
                if stack:
                    stack.pop()
                else:
                    del l[i]
                    i -= 1
            i += 1
        
        return ''.join([c for i, c in enumerate(l) if i not in stack])

