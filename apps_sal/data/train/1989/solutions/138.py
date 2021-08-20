class Solution:

    def longestAwesome(self, s: str) -> int:
        d = 0
        m = 0
        l = []
        l.append(d)
        dd = {}
        dd[0] = [0, 0]
        for i in range(len(s)):
            c = s[i]
            d = d ^ 1 << int(c)
            l.append(d)
            if d not in dd:
                dd[d] = [i + 1, i + 1]
            else:
                dd[d] = [min(dd[d][0], i + 1), max(dd[d][1], i + 1)]
        di = {}
        for i in range(2 ** 10):
            ll = {i}
            for k in range(10):
                ll.add(i ^ 1 << k)
            di[i] = ll
        for i in dd:
            for j in di[i]:
                if j in dd:
                    m = max(abs(dd[j][0] - dd[i][1]), m)
                    m = max(abs(dd[j][1] - dd[i][0]), m)
        return m
