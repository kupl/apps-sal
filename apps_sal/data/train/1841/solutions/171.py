class Solution:

    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        m = sorted(arr)[(len(arr) - 1) // 2]
        return [-x for (_, x) in sorted(((-abs(x - m), -x) for x in arr))[:k]]
