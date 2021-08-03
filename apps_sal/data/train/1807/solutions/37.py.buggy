class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def get_gcd(a, b):
            if b == 0:
                return a
            else:
                return get_gcd(b, a % b)


        fractions = set()
        for denominator in range(1, n + 1):
            for numerator in range(1, denominator):
                gcd = get_gcd(numerator, denominator)
                s_numerator = numerator // gcd
                s_denominator = denominator // gcd
                fraction = \"{}/{}\".format(s_numerator, s_denominator)
                fractions.add(fraction)

        return fractions

