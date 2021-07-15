from collections import defaultdict
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * len(nums)
        for pair in requests:
            count[pair[0]] += 1
            if pair[1] != len(nums) - 1:
                count[pair[1] + 1] -= 1
        dct = defaultdict(int)
        curr = 0
        total = 0
        for i in range(len(nums)):
            curr += count[i]
            if not curr:
                continue
            dct[curr] += 1
            total += 1
        nums.sort()
        res = 0
        items = sorted(list(dct.items()), reverse = True)
        for key, val in items:
            for i in range(val):
                res += key * nums[-1]
                nums.pop()
        return res % (10 ** 9 + 7)
        
        

