class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # observations:
        # - gcd can't be anything bigger than half the number
        result = []
        seen = set()
        for i in range(2, n + 1):
            for j in range(1, i):
                gcd = math.gcd(i, j)
                c_i = i
                c_i //= gcd
                j //= gcd
                if (j, c_i) not in seen:
                    seen.add((j, c_i))
                    result.append(\"{}/{}\".format(j, c_i))
        return result
