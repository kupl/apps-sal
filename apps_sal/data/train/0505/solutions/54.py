class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        par_stack = []
        for i, ch in enumerate(s):
            if ch == '(' or ch == ')':
                par_stack.append((i, ch))
                while len(par_stack) >= 2 and par_stack[-1][1] == ')' and par_stack[-2][1] == '(':
                    par_stack.pop()
                    par_stack.pop()
        
        invalid = {x[0]: True for x in par_stack}
        ret = [ch for i, ch in enumerate(s) if i not in invalid]
        return ''.join(ret)
