class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        if not arr or n == 0:
            return []

        arr.sort()
        m = arr[(n - 1) // 2]

        return sorted(arr, reverse=True, key=lambda x: (abs(x - m), x))[:k]
