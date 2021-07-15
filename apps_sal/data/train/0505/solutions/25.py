class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        stack = []  # save indexes of parenthesis
        out_s = ''
        i = 0
        
        for c in s:
            if c == ')':
                if len(stack) > 0:
                    stack.pop()
                    out_s += c
                    i += 1
            elif c == '(':
                stack.append(i)
                out_s += c
                i += 1
            else:
                out_s += c
                i += 1

        if len(stack)>0:
            out_s = [out_s[i] for i in range(len(out_s)) if i not in stack]

        return out_s
