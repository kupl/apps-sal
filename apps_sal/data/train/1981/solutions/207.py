class Solution:

    def maxSumRangeQuery(self, a: List[int], r: List[List[int]]) -> int:
        cnt = [0] * (len(a) + 1)
        for (s, e) in r:
            cnt[s] += 1
            cnt[e + 1] -= 1
        cnt = list(accumulate(cnt))
        return sum((x * y for (x, y) in zip(sorted(cnt[:-1]), sorted(a)))) % (10 ** 9 + 7)
