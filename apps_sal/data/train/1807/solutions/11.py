class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        r = set()

        for i in range(2, n + 1):
            for j in range(1, i):
                cd = gcd(i, j)
                r.add(str(j // cd) + '/' + str(i // cd))

        return r
