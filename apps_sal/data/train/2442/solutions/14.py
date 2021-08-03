class Solution:
    def sortString(self, s: str) -> str:
        x = sorted(s)
        res = ''
        r = 0
        while len(x) > 0:
            if r == 0:
                res += x[0]
                x.remove(x[0])
                i = 0
                while i < len(x):
                    if x[i] > res[-1]:
                        res += x[i]
                        x.remove(x[i])
                    else:
                        i += 1
                x = x[::-1]
                r = 1
            elif r == 1:
                res += x[0]
                x.remove(x[0])
                i = 0
                while i < len(x):
                    if x[i] < res[-1]:
                        res += x[i]
                        x.remove(x[i])
                    else:
                        i += 1
                x = x[::-1]
                r = 0
        return res
