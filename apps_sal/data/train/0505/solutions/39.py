class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        torem = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0 and s[stack[-1]] == '(':
                    stack = stack[:-1]
                else:
                    torem.append(i)
            elif s[i] == ']':
                if len(stack) > 0 and s[stack[-1]] == '[':
                    stack = stack[:-1]
                else:
                    torem.append(i)
            elif s[i] == '}':
                if len(stack) > 0 and s[stack[-1]] == '{':
                    stack = stack[:-1]
                else:
                    torem.append(i)
        stack.extend(torem)
        temp = [i for j, i in enumerate(list(s)) if j not in stack]
        return ''.join(temp)

