class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        for c in s:
            if c!=')': res += c
            else:
                if '(' in res:
                    idx = res.rfind('(')
                    res = res[:idx]+'L'+res[idx+1:]
                    res+=')'
        res = res.replace('(', '')
        res = res.replace('L', '(')
        return res

