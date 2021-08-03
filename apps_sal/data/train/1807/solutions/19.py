class Solution:
    def findGCD(self, a: int, b: int) -> int:
        a, b = (a, b) if a > b else (b, a)
        while a != 1 or b != 1:
            if a % b:
                a, b = b, a % b
            else:
                break

        return b

    def simplifiedFractions(self, n: int) -> List[str]:
        ret = set()
        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                gcd = self.findGCD(denominator, numerator)
                ret.add(f'{numerator // gcd}/{denominator // gcd}')

        return list(ret)
