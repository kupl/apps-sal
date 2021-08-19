import queue


class Solution:

    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        streak = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                streak += 1
            else:
                streak = 0
            if streak == (k - 1) * m:
                return True
        return False
