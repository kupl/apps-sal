class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        if n == 1:
            return []

        def gcd(a, b):
            while b > 0:
                r = a % b
                a = b
                b = r
            return a

        ret = []
        for deno in range(2, n + 1):
            for nume in range(1, deno):
                g = gcd(deno, nume)
                n = nume // g
                d = deno // g
                val = str(n) + '/' + str(d)
                if val not in ret:
                    ret.append(val)
        return ret
