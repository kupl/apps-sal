class Solution:

    def findTheDistanceValue(self, A: List[int], B: List[int], d: int) -> int:
        return sum((1 - any([abs(a - b) <= d for b in B]) for a in A))
