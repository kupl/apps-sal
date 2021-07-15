class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        
        for char in s:
            if char == '(':
                stack.append('')
            elif char == ')':
                temp = stack.pop()[::-1]
                stack[-1] += temp
            else:
                stack[-1] += char
        
        return ''.join(stack)
