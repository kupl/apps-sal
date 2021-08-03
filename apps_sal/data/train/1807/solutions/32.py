class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = set()
        for m in range(2, n + 1):
            for i in range(1, m):
                d = math.gcd(i, m)
                if d > 1:
                    ans.add(f'{i//d}/{m//d}')
                else:
                    ans.add(f'{i}/{m}')
        return ans
