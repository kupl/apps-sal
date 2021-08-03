class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l, stack = 0, []
        for i in s:
            if i not in ('()'):
                stack.append(i)
            elif i == '(':
                l += 1
                stack.append('(')
            else:
                if l == 0:
                    continue
                else:
                    stack.append(')')
                    l -= 1
        i = len(stack) - 1
        while l > 0 and i >= 0:
            if stack[i] == '(':
                stack[i] = ''
                l -= 1
            i -= 1
        return ''.join(stack)
