class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        div = len(arr) // 4
        for i in range(len(arr) - div):
            if arr[i] == arr[i + div]:
                return arr[i]
