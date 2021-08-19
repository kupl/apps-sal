class Solution:

    def partition(self, arr, pi):
        (less, equal, high) = ([], [], [])
        for i in arr:
            if i < pi:
                less.append(i)
            if i == pi:
                equal.append(i)
            if i > pi:
                high.append(i)
        return (less, equal, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) < 1:
            return nums
        pivot = nums[0]
        (less, equal, high) = self.partition(nums, pivot)
        return self.sortArray(less) + equal + self.sortArray(high)
