class Solution:
    # def __init__(self):

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            l1 = nums[:len(nums) // 2]
            l2 = nums[len(nums) // 2:]
            L = self.mergeSort(l1)
            R = self.mergeSort(l2)

            sorted_list = []
            i = j = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    sorted_list.append(L[i])
                    i += 1
                else:
                    sorted_list.append(R[j])
                    j += 1

            while i < len(L):
                sorted_list.append(L[i])
                i += 1
            while j < len(R):
                sorted_list.append(R[j])
                j += 1
            return sorted_list

        return nums
