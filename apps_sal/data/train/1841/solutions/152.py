class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        m = arr[(len(arr) - 1) // 2]
        return heapq.nlargest(k, [n for n in arr[::-1]], key=lambda x: abs(x - m))
