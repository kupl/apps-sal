class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nos):
            if len(nos) > 1:
                mid = len(nos) // 2
                left = nos[mid:]
                right = nos[:mid]
                left = mergeSort(left)
                right = mergeSort(right)
                nos = []
                while left and right:
                    if left[0] < right[0]:
                        nos.append(left[0])
                        left.pop(0)
                    else:
                        nos.append(right[0])
                        right.pop(0)
                for i in left:
                    nos.append(i)
                for j in right:
                    nos.append(j)
            return nos

        return mergeSort(nums)
