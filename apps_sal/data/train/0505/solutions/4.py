class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        stack = []
        for ele in s:
            if ele not in '()':
                res.append(ele)
            elif ele == '(':
                stack.append(ele)
                res.append(ele)
            elif ele == ')':
                if stack != [] and stack[-1] == '(':
                    res.append(ele)
                    stack.pop()
        if stack == []:
            return ''.join(res)
        else:
            i = len(res) - 1
            while stack:
                if res[i] == stack[-1]:
                    stack.pop()
                    res = res[:i] + res[i + 1:]
                i = i - 1
            return ''.join(res)
