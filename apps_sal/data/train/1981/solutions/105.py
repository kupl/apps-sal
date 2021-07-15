from collections import defaultdict

MOD = int(1e9 + 7) 

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        temp = [0 for _ in range(len(nums))]
        sum_ = 0
        for r in requests:
            temp[r[0]] += 1
            if r[1]+1 < len(nums):
                temp[r[1]+1] -= 1
            
        temp2 = []
        count = 0
        for x in temp:
            count += x
            temp2.append(count)
        sorted_counter = sorted(temp2, reverse=True)
        
        # print(sorted_nums)
        # print(len(sorted_nums))
        # print(temp)
        # print(len(temp))
        # print(sorted_counter)
        
        for counter in sorted_counter:
            sum_ += (counter * sorted_nums.pop(0)) % MOD
        
        # print(sorted_nums)
        
        return sum_ % MOD
            

