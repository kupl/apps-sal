class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        # r = len(arr) - 1
        while arr[l] < arr[l + 1]:
            l += 1
        return l
        # while l < r:
        #     mid = (l + r)//2
        #     if arr[mid] < arr[mid + 1]:
        #         l = mid + 1
        #     else:
        #         r = mid
        # return r
        # while l < r:
        #     if arr[r-1] >= arr[r]:
        #         r -= 1
        #     if arr[l + 1] >= arr[l]:
        #         l += 1
        # return r

