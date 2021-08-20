class Solution:

    def maxSumRangeQuery(self, a: List[int], r: List[List[int]]) -> int:
        r1 = []
        for (s, e) in r:
            r1.extend([(s, 1), (e, -1)])
        r = r1
        r.sort(reverse=True)
        op = 0
        n = len(a)
        cand = []
        cur_start = 0
        cur_end = -1
        cnt = [0] * n
        for i in range(n):
            cl = 0
            while r and r[-1][0] == i:
                p = r.pop()[1]
                op += p == 1
                cl += p == -1
            cnt[i] = op
            op -= cl
        cnt.sort()
        a.sort()
        return sum((x * y for (x, y) in zip(cnt, a))) % (10 ** 9 + 7)
