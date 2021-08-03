class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        asc = True
        ans = ''
        while d:
            for i in sorted(d) if asc else sorted(d, reverse=True):
                ans += i
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
            asc ^= True
        return ans
