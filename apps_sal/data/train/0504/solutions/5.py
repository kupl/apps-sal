class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                if stack:
                    stack.pop()
                for k in temp:
                    stack.append(k)
            else:
                 stack.append(i)
        return ''.join(stack)

