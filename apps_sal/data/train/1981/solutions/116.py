class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        ranks = [0] * (len(nums) + 1)
        requests.sort()
        
        for start, end in requests:
            ranks[start] += 1
            ranks[end + 1] -= 1
        
        nums.sort()
        for i in range(1, len(nums) + 1):
            ranks[i] += ranks[i - 1]
        
        ranks = ranks[:len(nums)]
        
        return sum(x * y for x, y in zip(sorted(nums), sorted(ranks))) % MOD
