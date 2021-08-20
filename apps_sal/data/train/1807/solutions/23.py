class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:
        l = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) < 2:
                    l += [f'{j}/{i}']
        return l
