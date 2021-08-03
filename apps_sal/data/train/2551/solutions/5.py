class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                j = stack.pop()
                if (j == '(' and i != ')') or (j == '[' and i != ']') or (j == '{' and i != '}'):
                    return False
        return len(stack) == 0
