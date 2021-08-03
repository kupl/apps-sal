class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1, arr2):
            if not arr1:
                return arr2
            if not arr2:
                return arr1

            res = []
            a1 = 0
            a2 = 0

            while a1 < len(arr1) or a2 < len(arr2):
                if a1 == len(arr1):
                    res.append(arr2[a2])
                    a2 += 1
                    continue
                if a2 == len(arr2):
                    res.append(arr1[a1])
                    a1 += 1
                    continue

                if arr1[a1] < arr2[a2]:
                    res.append(arr1[a1])
                    a1 += 1
                else:
                    res.append(arr2[a2])
                    a2 += 1
            return res

        def mergesort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            return merge(left, right)
        return mergesort(nums)
