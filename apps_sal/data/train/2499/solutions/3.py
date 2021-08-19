class Solution:

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        hashmap = {}
        for i in range(len(deck)):
            try:
                hashmap[deck[i]] += 1
            except:
                hashmap[deck[i]] = 1
        vals = set(list(hashmap.values()))
        gcd_val = next(iter(vals))
        for i in vals:
            gcd_val = gcd(gcd_val, i)
            if gcd_val == 1:
                return False
        return True
