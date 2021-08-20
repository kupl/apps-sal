class Solution:

    def isMonotonic(self, arr: List[int]) -> bool:
        f = True
        n = len(arr)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                f = False
                break
        if f:
            return True
        r = True
        for i in range(n - 1):
            if arr[i] < arr[i + 1]:
                r = False
                break
        return r
