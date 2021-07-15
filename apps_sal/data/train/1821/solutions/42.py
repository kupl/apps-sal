class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        nums_before = 0
        for k, v in sorted(counts.items(), key=lambda x: x[0]):
            nums_before += v
            counts[k] = nums_before-1
        out = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            out[counts[nums[i]]] = nums[i]
            counts[nums[i]] -= 1
        return out
