class Solution:

    def maxSumRangeQuery(self, a: List[int], r: List[List[int]]) -> int:
        ends = []
        for (s, e) in r:
            ends.extend([(s, 1), (e, -1)])
        ends.sort(reverse=True)
        (n, op) = (len(a), 0)
        cnt = [0] * n
        for i in range(n):
            cl = 0
            while ends and ends[-1][0] == i:
                p = ends.pop()[1]
                op += p == 1
                cl += p == -1
            cnt[i] = op
            op -= cl
        cnt.sort()
        a.sort()
        return sum((x * y for (x, y) in zip(cnt, a))) % (10 ** 9 + 7)
