class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            result = []
            while len(left) != 0 and len(right) != 0:
                l = left[0]
                r = right[0]
                if r < l:
                    result.append(right.pop(0))
                else:
                    result.append(left.pop(0))
            return result + left + right

        def mergeSort(arr):
            if len(arr) < 2:
                return arr[:]
            else:
                mid = len(arr) // 2
                left = mergeSort(arr[:mid])
                right = mergeSort(arr[mid:])
                return merge(left, right)

        return mergeSort(nums)
