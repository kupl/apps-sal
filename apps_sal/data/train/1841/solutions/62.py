class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        median = sorted(arr)[(len(arr) - 1) // 2]
        return heapq.nsmallest(k, arr, key=lambda x: (-abs(x - median), -x))
