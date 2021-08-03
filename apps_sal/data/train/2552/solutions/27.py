class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l = len(arr) // 4
        for i in range(len(arr) - l):
            if arr[i] == arr[i + l]:
                return arr[i]
