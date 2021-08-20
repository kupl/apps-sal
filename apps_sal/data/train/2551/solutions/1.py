class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        (stack, lookup) = ([], {'(': ')', '{': '}', '[': ']'})
        for parenthese in s:
            if parenthese in lookup.keys():
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0
