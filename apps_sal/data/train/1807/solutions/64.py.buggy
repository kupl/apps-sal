def gcd(a, b):\r
    # Everything divides 0\r
    if a == 0:\r
        return b\r
    if b == 0:\r
        return a\r
    # base case\r
    if a == b:\r
        return a\r
    # a is greater\r
    if a > b:\r
        return gcd(a - b, b)\r
    return gcd(a, b - a)\r
\r
\r
class Solution:\r
    def simplifiedFractions(self, n: int) -> List[str]:\r
        finals = []\r
        for i in range(1, n):\r
            for j in range(i, n + 1):\r
                if i != j:\r
                    g = gcd(i, j)\r
                    finals.append(\"{}/{}\".format(i // g, j // g))\r
        return list(set(finals))\r
\r

