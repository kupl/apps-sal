class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        arr = A
        i = 1
        while i < len(arr):
            if arr[i - 1] < arr[i]:
                i += 1
            else:
                break
        if i == 1 or i == len(arr):
            return False
        while i < len(arr):
            if arr[i - 1] > arr[i]:
                i += 1
            else:
                return False
        return True
