class Solution:

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = list(s)
        stack = []
        if l[0] == ')' or l[0] == ']' or l[0] == '}' or (len(l) < 2):
            return False
        else:
            stack.append(l[0])
            l = l[1:]
        while stack != [] or l != []:
            if l == []:
                return False
            else:
                if l[0] == '(' or l[0] == '[' or l[0] == '{':
                    stack.append(l[0])
                elif stack == []:
                    return False
                elif stack[-1] == '(' and l[0] == ')':
                    stack.pop()
                elif stack[-1] == '[' and l[0] == ']':
                    stack.pop()
                elif stack[-1] == '{' and l[0] == '}':
                    stack.pop()
                else:
                    return False
                l = l[1:]
        return True
