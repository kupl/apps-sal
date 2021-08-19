class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        answer = 0
        for (k, v) in counter.items():
            answer += v * (v - 1) // 2
        return answer
