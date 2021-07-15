class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ')':
                stack.append(i)
            else:
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack[-1] == '(':
                    stack.pop()
                for k in temp:
                    stack.append(k)
        return ''.join(stack)

