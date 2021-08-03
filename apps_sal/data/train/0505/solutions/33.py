from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # forward pass to find invalid closed paren
        toremove = []
        openP = deque()
        for i in range(len(s)):
            if s[i] == '(':
                openP.append(i)
            elif s[i] == ')':
                if len(openP) > 0:
                    openP.pop()
                else:
                    toremove.append(i)
        # backward pass
        closeP = deque()
        for i in range(len(s)):
            if s[len(s) - i - 1] == ')':
                closeP.append(len(s) - i - 1)
            elif s[len(s) - i - 1] == '(':
                if len(closeP) > 0:
                    closeP.pop()
                else:
                    toremove.append(len(s) - i - 1)
        ret = ''
        for i in range(len(s)):
            if i not in toremove:
                ret += s[i]
        return ret
