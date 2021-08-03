class Solution:
    def maxSumRangeQuery(self, a: List[int], r: List[List[int]]) -> int:
        ends = []
        for s, e in r:
            ends.extend([(s, 1), (e + 1, -1)])
        ends.sort(reverse=True)
        n, op = len(a), 0
        cnt = [0] * n
        for i in range(n):
            while ends and ends[-1][0] == i:
                op += ends.pop()[1]
            cnt[i] = op
        return sum(x * y for x, y in zip(sorted(cnt), sorted(a))) % (10**9 + 7)
