class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right = 0, 0
        result = []
        for i, c in enumerate(s):
            if c == '(':
                left += 1
                result.append(c)
            elif c == ')':
                if right + 1 > left:
                    continue
                else:
                    right += 1
                    result.append(c)
            else:
                result.append(c)
        while left > right:
            i = len(result) - result[::-1].index('(') - 1
            result = result[:i] + result[i + 1:]
            left -= 1

        return ''.join(result)
