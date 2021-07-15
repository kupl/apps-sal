class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def binary_search(t):
            lo = 0
            hi = len(arr)
            while lo <= hi:
                mid = lo + (hi-lo)//2
                if mid >=len(arr):
                    return False
                if arr[mid] == t:
                    return True

                if arr[mid] > t:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
        count = 0
        for num in range(1, arr[-1]+k+1):
            if not binary_search(num):
                count+=1
                if count == k:
                    return num
        return -1
