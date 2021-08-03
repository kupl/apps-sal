class Solution:
    def maxSumRangeQuery(self, A: List[int], req: List[List[int]]) -> int:
        n = len(A)
        count = [0] * (n + 1)

        for i, j in req:
            count[i] += 1
            count[j + 1] -= 1

        for i in range(1, n + 1):
            count[i] += count[i - 1]

        res = 0
        A.sort()
        count.pop()
        count.sort()

        for v, c in zip(count, A):
            res += v * c

        return res % (pow(10, 9) + 7)

        # n = len(A)
        # count = [0] * (n + 1)
        # for i, j in req:
        #     count[i] += 1
        #     count[j + 1] -= 1
        # for i in range(1, n + 1):
        #     count[i] += count[i - 1]
        # res = 0
        # for v, c in zip(sorted(count[:-1]), sorted(A)):
        #     res += v * c
        # return res % (10**9 + 7)
