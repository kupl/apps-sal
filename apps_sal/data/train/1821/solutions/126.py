class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr):
            
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            
            newArr = []
            i = 0
            j = 0
            while i < len(left) or j < len(right):
                if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                    newArr.append(left[i])
                    i += 1
                elif i >= len(left) or (j < len(right) and right[j] <= left[i]):
                    newArr.append(right[j])
                    j += 1
            
            return newArr
        
        return mergeSort(nums)

