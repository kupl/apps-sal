class Solution:

    def simplifiedFractions(self, n: int) -> List[str]:

        def gcd(a, b):
            for i in range(a):
                if b % (a - i) == 0 and a % (a - i) == 0:
                    return a - i
        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if gcd(j, i) == 1:
                    ans.append(f'{j}/{i}')
        return ans
