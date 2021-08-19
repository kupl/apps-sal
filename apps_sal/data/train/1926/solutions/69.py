class Solution:

    def closestDivisors(self, num: int) -> List[int]:

        def getDiv(n):
            d1s = 1
            d2s = n
            s = n - 1
            d1 = 1
            d2 = n
            while d1 <= d2:
                d1 += 1
                if n % d1 == 0:
                    d1s = d1
                    d2s = n // d1
                d2 = n / d1
            return (d1s, d2s)
        (v1, v2) = getDiv(num + 1)
        (z1, z2) = getDiv(num + 2)
        vdif = v2 - v1
        zdif = z2 - z1
        print((v1, v2, z1, z2))
        print((vdif, zdif))
        if vdif > zdif:
            return [z1, z2]
        else:
            return [v1, v2]
