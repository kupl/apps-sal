class Solution:
    def specialArray(self, nums: List[int]) -> int:
        low, high = 0, len(nums)
        while low <= high:
            mid = (low + high) // 2
            cnt = 0
            for i in nums:
                if i >= mid: cnt += 1
            if cnt == mid:
                return mid
            elif cnt > mid: low = mid + 1
            else: high = mid - 1
        return -1
