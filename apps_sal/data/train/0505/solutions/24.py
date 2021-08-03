class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stacklp = []
        stackrp = []
        for i in range(len(s)):
            if s[i] == '(':
                stacklp.append(i)
            elif s[i] == ')':
                if stacklp != []:
                    stacklp.pop()
                else:
                    stackrp.append(i)

        stack = sorted(stacklp + stackrp)
        res = ''
        for i in range(len(s)):
            if i not in stack:
                res = res + s[i]

        return res
