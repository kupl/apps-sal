class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        d = n // 4
        for i in range(n - 4):
            if arr[i] == arr[i + d]:
                return arr[i]
        return arr[-1]
