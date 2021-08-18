class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        return sorted(arr, key=lambda x: (abs(x - m), x), reverse=True)[:k]
