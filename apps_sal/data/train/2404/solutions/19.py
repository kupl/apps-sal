class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = []

        for i in range(1, arr[-1] + 1):
            nums.append(i)

        for i in range(len(nums)):
            if nums[i] not in arr:
                k -= 1
            if k == 0:
                return nums[i]

        val = arr[-1]
        while k != 0:
            val += 1
            k -= 1

        return val
