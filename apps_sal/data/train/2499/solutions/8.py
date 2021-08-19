from functools import reduce


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        vals = list(collections.Counter(deck).values())
        return reduce(gcd, vals) >= 2
