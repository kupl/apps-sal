class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # permutation
        # requests where requests[i] = [starti, endi]
        # ith request asks for sum of 
        from operator import add
        lenn = len(nums)
        ranks = [0] * (lenn + 1)
        for i, j in requests:
            ranks[i]  += 1
            ranks[j+1] -= 1
        for i in range(1, lenn + 1):
            ranks[i] += ranks[i-1]
        ranks = ranks[:lenn]
        return sum(x*y for x, y in zip(sorted(ranks), sorted(nums))) % (10**9 + 7)
    

