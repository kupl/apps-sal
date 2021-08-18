class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(0, len(arr) - (k - 1) * m - m + 1):
            found = True
            for j in range(0, m):
                for n in range(1, k):
                    if arr[i + j] != arr[m * n + i + j]:
                        found = False
            if found:
                return True
        return False
