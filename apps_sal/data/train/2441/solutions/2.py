class Solution:

    def makeGood(self, s: str) -> str:
        res = []
        for i in s:
            if not res:
                res.append(i)
            elif res[-1].islower() and res[-1].upper() == i:
                res.pop()
            elif res[-1].isupper() and res[-1].lower() == i:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
