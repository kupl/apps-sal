class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:

        def gcd(a, b):
            if a < b:
                a, b = b, a
            while b != 0:
                a, b = b, a % b
            return a

        # print (gcd(6, 4))

        sol = []
        for denom in range(2, n + 1):
            for numer in range(1, denom):
                if numer == 1 or gcd(numer, denom) == 1:
                    sol.append(str(numer) + '/' + str(denom))
        return sol
