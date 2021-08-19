class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ret = set()

        def gcd(a, b):
            while True:
                q = a // b
                r = a - b * q
                if r == 0:
                    return b
                a = b
                b = r

        for i in range(2, n + 1):
            for j in range(1, i):
                t = gcd(i, j)
                #print(i, j, t)
                ret.add(f'{j//t}/{i//t}')
        return list(ret)
