class Solution:

    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                word = stack.pop()[::-1]
                stack[-1] += word
            else:
                stack[-1] += c
        return ''.join(stack)
