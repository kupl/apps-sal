class Solution:

    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = ''
        for c in s:
            if c == '(':
                stack.append(curr)
                curr = ''
                stack.append('(')
            elif c == ')':
                stack.append(curr)
                curr = ''
                aux = ''
                while stack and stack[-1] != '(':
                    aux = stack.pop() + aux
                stack.pop()
                stack.append(aux[::-1])
            else:
                curr += c
        if curr:
            stack.append(curr)
        return ''.join(stack)
