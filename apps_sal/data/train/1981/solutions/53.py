class Solution:
    def maxSumRangeQuery(self, n: List[int], r: List[List[int]]) -> int:
        r.sort()
        n.sort(reverse=True)
        s = sorted([x for x, y in r])
        t = sorted([y for x, y in r])
        c = collections.Counter()
        x = 0
        si, ti = 0, 0
        for i in range(s[0], t[-1] + 1):
            while si < len(s) and s[si] == i:
                x += 1
                si += 1
            c[x] += 1
            while ti < len(t) and t[ti] == i:
                x -= 1
                ti += 1
        res = 0
        print(s, t)
        print(c.most_common())
        ni = 0
        for k in sorted(c.elements(), reverse=True):
            res += k * n[ni]
            ni += 1

        return res % (10**9 + 7)
