class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(0, len(arr) - (k - 1) * m - m + 1):
            found = True
            j = 0
            while found and j < m:
                n = 1
                while found and n < k:
                    if arr[i + j] != arr[m * n + i + j]:
                        found = False
                    n += 1
                j += 1
            if found:
                return True
        return False
