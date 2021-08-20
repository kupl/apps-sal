class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        out = []
        left_pos = []
        l = 0
        for c in s:
            if c != '(' and c != ')':
                out.append(c)
                l += 1
            elif c == '(':
                out.append(c)
                stack.append(c)
                left_pos.append(l)
                l += 1
            elif stack:
                out.append(c)
                stack = stack[:-1]
                left_pos = left_pos[:-1]
                l += 1
        out_string = ''
        for i in range(len(out)):
            if i not in left_pos:
                out_string += out[i]
        return out_string
