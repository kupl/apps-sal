class Solution:

    def heightChecker(self, h: List[int]) -> int:
        return sum([x != y for (x, y) in zip(h, sorted(h))])
