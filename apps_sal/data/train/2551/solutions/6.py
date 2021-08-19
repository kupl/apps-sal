class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if stack[0] == ')' or stack[0] == ']' or stack[0] == '}':
                return False
            if stack[-1] == ')':
                if stack[-2] == '(':
                    stack.pop()
                    stack.pop()
            elif stack[-1] == ']':
                if stack[-2] == '[':
                    stack.pop()
                    stack.pop()
            elif stack[-1] == '}':
                if stack[-2] == '{':
                    stack.pop()
                    stack.pop()
        if stack == []:
            return True
        else:
            return False
