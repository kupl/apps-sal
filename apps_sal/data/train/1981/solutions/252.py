from collections import Counter
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
                
        # 1a. Find optimal permutation of nums. O(N^2) / O(requests * len(requests))
            # Create Counter with number of entries for each number. 
            # Sort # of requests from large to small
        # c = {i : 0 for i, v in enumerate(nums)}
        # for r in requests:
        #     for i in range(r[0], r[1] + 1):
        #         c[i] += 1
        # requests_per_num = [c[k] for k in c]
        # requests_per_num.sort(reverse=True) 
        
        # 1b. Let's try to do this in O(N) + O(R) time. 
        # Create Counters of start / end values of requests.
        start = Counter([r[0] for r in requests])
        end = Counter([r[1] for r in requests])

        # Loop through possible nums.
        running_sum = 0
        requests_per_num = []
        
        # Use counter to update num requests. 
        for i, n in enumerate(nums):
            running_sum += start[i]
            running_sum -= end[i - 1]
            requests_per_num.append(running_sum)
        requests_per_num.sort(reverse=True) 
            
        # 2. Order numbers to match most common requests.
        nums_copy = [n for n in nums]
        nums_copy.sort(reverse=True)
        
        # Compute sum.
        max_sum = 0
        for n, r in zip(nums_copy, requests_per_num):
            max_sum += n * r
            
        # Return max sum mod 10 ** 9 + 7
        return max_sum % (10 ** 9 + 7)
