class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        val = list(count.values())
        gcd = val[0]
        for i in val[1:]:
            gcd = math.gcd(i, gcd)
        return gcd >= 2
