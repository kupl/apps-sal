class Solution:
    def _get_median(self, arr):
        mid = int((len(arr) - 1) / 2)
        return arr[mid]

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        median = self._get_median(arr)
        arr = sorted([(abs(x - median), x) for x in arr], reverse=True)[:k]
        return [x for rank, x in arr]
