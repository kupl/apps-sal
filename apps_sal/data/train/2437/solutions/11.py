class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr)):
            if i + m * k - 1 >= len(arr):
                break
            if arr[i:i + m] * k == arr[i:i + m * k]:
                return True
        return False
