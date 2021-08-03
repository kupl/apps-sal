class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        m = sorted(arr)[(n - 1) // 2]
        return sorted(arr, key=lambda x: (abs(x - m), x), reverse=True)[:k]
