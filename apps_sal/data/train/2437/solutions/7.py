class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        for i in range(len(arr) - m + 1):
            p = arr[i:i + m]
            c = 1
            for j in range(i + m, len(arr) - m + 1):
                if arr[j:j + m] == p:
                    c += 1
                    if c == k:
                        return True
                else:
                    break
        return False
