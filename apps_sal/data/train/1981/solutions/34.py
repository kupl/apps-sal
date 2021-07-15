class Solution:
    def maxSumRangeQuery(self, a: List[int], req: List[List[int]]) -> int:
        n = len(a)
        count = [0] * (n + 1)
        for i, j in req:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        res = 0
        for count, value in zip(sorted(count[:-1]), sorted(a)):
            res += count * value
        return res % (10 ** 9 + 7)
