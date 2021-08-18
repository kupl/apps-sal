class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        def min_d(num, arr):
            left = 0
            right = len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(arr):
                return num - arr[-1]
            elif left == 0:
                return arr[0] - num
            return min(arr[left] - num, num - arr[left - 1])

        arr2.sort()
        distance = 0
        for num in arr1:
            if min_d(num, arr2) > d:
                distance += 1

        return distance
