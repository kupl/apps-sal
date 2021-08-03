class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        c = Counter(deck)
        cur_g = 0
        for i in c.values():
            cur_g = gcd(cur_g, i)
        return cur_g > 1
