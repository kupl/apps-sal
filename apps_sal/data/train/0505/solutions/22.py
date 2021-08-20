class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        parens = []
        to_remove = set()
        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if not parens:
                    to_remove.add(i)
                else:
                    parens.pop()
            elif c == '(':
                parens.append(i)
        string = ''
        for i in range(len(s)):
            if i in to_remove or i in parens:
                continue
            else:
                string += s[i]
        return string
