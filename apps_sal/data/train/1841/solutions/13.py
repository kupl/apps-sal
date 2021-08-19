class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if k == n:
            return arr
        arr.sort()
        med = arr[(len(arr) - 1) // 2]
        sorted_diff = sorted(arr, key=lambda x: abs(x - med))
        return sorted_diff[-k:]
