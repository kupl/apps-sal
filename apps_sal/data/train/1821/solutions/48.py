class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums, start, end):
            if start >= end:
                return
            mid = start + (end - start) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            L = [0] * (mid - start + 1)
            R = [0] * (end - mid)
            n1 = len(L)
            n2 = len(R)
            for i in range(n1):
                L[i] = nums[start + i]
            for j in range(n2):
                R[j] = nums[mid + 1 + j]
            i = j = 0
            for _ in range(start, end + 1):
                if j >= n2 or (i < n1 and L[i] <= R[j]):
                    nums[start + i + j] = L[i]
                    i += 1
                else:
                    nums[start + i + j] = R[j]
                    j += 1
        mergeSort(nums, 0, len(nums) - 1)
        return nums
