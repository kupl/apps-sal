class BinaryIndexedTree:
    """ index range from 0 to n-1"""

    def __init__(self, n):
        n += 1
        self.data = [0] * n
        self.n = n

    def add(self, index, value):
        index += 1
        while index < self.n:
            self.data[index] += value
            index += index & -index

    def prefix(self, index):
        index += 1
        res = 0
        while index:
            res += self.data[index]
            index ^= index & -index
        return res


class Solution:

    def maxSumRangeQuery(self, nums: List[int], query: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        BIT = BinaryIndexedTree(n + 1)
        for (l, r) in query:
            BIT.add(l, 1)
            BIT.add(r + 1, -1)
        count_index = []
        for i in range(n):
            count_index.append((BIT.prefix(i), i))
        count_index.sort()
        nums.sort()
        ans = 0
        for ((ct, _), v) in zip(count_index, nums):
            ans += ct * v
            ans %= MOD
        return ans
