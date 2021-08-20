class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        bit = [0] * (n + 1)

        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def insert(key, value):
            while key <= n:
                bit[key] += value
                key += key & -key
        for request in requests:
            insert(request[0] + 1, 1)
            insert(request[1] + 2, -1)
        vals = sorted([query(i + 1) for i in range(n)])
        return sum((x * y for (x, y) in zip(vals, nums))) % 1000000007
