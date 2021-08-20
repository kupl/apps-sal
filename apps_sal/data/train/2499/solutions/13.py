class Solution:

    def hasGroupsSizeX(self, deck):

        def gcd(a, b):
            while b:
                (a, b) = (b, a % b)
            return a
        count = [*list(Counter(deck).values())]
        g = count[0]
        for i in range(len(count)):
            g = gcd(g, count[i])
            if g == 1:
                return False
        return True
