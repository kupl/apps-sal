class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        \"\"\"
 
        \"\"\"
        import collections
        request_idx_mapping = collections.defaultdict(int)
        
        
        for open_idx, close_idx in requests:
            request_idx_mapping[open_idx] += 1
            request_idx_mapping[close_idx + 1] -= 1
        request_freq = [0 for _ in range(len(nums))]
        idxes = [i for i in range(len(nums))]
        current_requests = 0
        for idx in range(len(nums)):
            current_requests += request_idx_mapping[idx]
            
            request_freq[idx] = current_requests
        idxes.sort(key=lambda idx: request_freq[idx], reverse=True)
        nums.sort()
        
        result = 0
        
        for idx in idxes:
            freq = request_freq[idx]
            num = nums.pop()
            result += freq*num
        MOD = 10 ** 9 + 7
        return result % MOD
            
