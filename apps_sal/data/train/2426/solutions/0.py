class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        if len(A) == 1:
            return 0
        _min = min(A)
        _max = max(A)
        if _max - K <= _min + K:
            return 0
        return _max - _min - 2 * K
