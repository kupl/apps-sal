class Solution:
    def findTheDistanceValue(self, a1: List[int], a2: List[int], d: int) -> int:
        x = set(a1)
        x -= {a + i for a in a2 for i in range(-d, d + 1)}
        return sum(n in x for n in a1)
