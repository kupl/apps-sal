class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        l = len(arr)
        while i + 1 < l and arr[i] < arr[i + 1]:
            i += 1
        if i == 0 or i == l - 1:
            return False
        while i + 1 < l and arr[i] > arr[i + 1]:
            i += 1
        return i == l - 1
