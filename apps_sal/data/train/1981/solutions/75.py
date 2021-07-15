class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        '''
        Count the frequency of each index and re-arrange
        '''
        freq = [0] * (len(nums) + 1)
        for l in requests:
            freq[l[0]] += 1
            freq[l[1]+1] -= 1
        for i in range(1, len(freq)):
            freq[i] += freq[i-1]
        ans = 0
        for x, y in zip(sorted(freq[:-1]), sorted(nums)):
            ans += x * y
        return ans % 1000000007

