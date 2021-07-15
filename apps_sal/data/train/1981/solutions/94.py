class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        N = len(nums)
        index_weight = collections.defaultdict(int)
        for s, e in requests:
            index_weight[s] += 1
            index_weight[e + 1] -= 1
        
        for i in range(1, N):
            index_weight[i] += index_weight[i - 1]
        
        print(index_weight)
        
        sorted_w = sorted(list(index_weight.keys()), key=lambda i: -index_weight[i])
        sorted_n = sorted(nums, key=lambda n: -n)
        
        ans = 0
        i = 0
        for idx in sorted_w:
            if index_weight[idx] > 0:
                ans += index_weight[idx] * sorted_n[i]
                i += 1
        
        return ans % (10 ** 9 + 7)

