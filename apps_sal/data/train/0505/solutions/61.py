class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        left = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    continue
            stack.append(i)
        if left == 0:
            return ''.join(stack)
        ans = ''
        while stack:
            val = stack.pop()
            if left > 0 and val == '(':
                left -= 1
                continue
            ans = val + ans
        return ans
