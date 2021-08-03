class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # MergeSort
        def merge(nums, lo, hi):
            mid = (lo + hi) // 2
            # [lo, mid] and [mid+1, hi] are already sorted
            i, j = lo, mid + 1
            sortedNums = []
            while i <= mid and j <= hi:
                if nums[i] < nums[j]:
                    sortedNums.append(nums[i])
                    i += 1
                else:
                    sortedNums.append(nums[j])
                    j += 1

            while i <= mid:
                sortedNums.append(nums[i])
                i += 1

            while j <= hi:
                sortedNums.append(nums[j])
                j += 1
            nums[lo:hi + 1] = sortedNums

        def mergeSort(nums, lo, hi):
            if hi - lo == 0:
                return

            mid = (lo + hi) // 2

            mergeSort(nums, lo, mid)
            mergeSort(nums, mid + 1, hi)
            # Both left and right portions are sorted
            merge(nums, lo, hi)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
