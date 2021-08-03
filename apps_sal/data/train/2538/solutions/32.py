class Solution:
    def countLargestGroup(self, n: int) -> int:
        d, c = {}, 0
        for i in range(1, n + 1):
            if i % 10 == 0:
                c = sum(map(int, str(i)))
                d[c] = d.get(c, 0) + 1
            else:
                c += 1
                d[c] = d.get(c, 0) + 1
        res, m = 0, 0
        for v in list(d.values()):
            if v > m:
                res = 1
                m = v
            elif v == m:
                res += 1
        return res
