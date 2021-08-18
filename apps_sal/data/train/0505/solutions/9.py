class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        p = []
        for index, item in enumerate(s):
            if item == '(':
                stack.append(index)
            elif item == ')' and stack:
                p.append([stack.pop(), index])

        s = s.replace(')', '_').replace('(', '_')
        for [l, r] in p:
            s = s[:l] + '(' + s[l + 1:r] + ')' + s[r + 1:]
        return s.replace('_', '')
