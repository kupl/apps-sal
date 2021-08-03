class Solution:
    def reorderSpaces(self, text: str) -> str:
        wds = text.split()
        sc = text.count(' ')
        if len(wds) == 1:
            return text.strip(' ') + ' ' * sc
        nwds = len(wds)
        s = nwds - 1
        res = sc // s
        rem = sc - res * s
        ans = ''
        for i in wds[:-1]:
            ans += i
            ans += ' ' * res
        ans += wds[-1]
        ans += ' ' * rem
        return ans
