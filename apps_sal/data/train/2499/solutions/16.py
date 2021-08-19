class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        counter = collections.Counter(deck)
        # check if X>=2

        for i in counter:
            if(counter[i] < 2):
                return False
        cur_gcd = 0
        for i in counter:
            cur_gcd = gcd(cur_gcd, counter[i])
        if cur_gcd == 1:
            return False
        return True
