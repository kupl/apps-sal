import sys


def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))


class mint:
    def __init__(self, x):
        self.__x = x % md

    def __repr__(self):
        return str(self.__x)

    def __neg__(self):
        return mint(-self.__x)

    def __add__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x + other)

    def __sub__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x - other)

    def __rsub__(self, other):
        return mint(other - self.__x)

    def __mul__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x * other)

    __radd__ = __add__
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, mint):
            other = other.__x
        return mint(self.__x * pow(other, md - 2, md))

    def __rtruediv__(self, other):
        return mint(other * pow(self.__x, md - 2, md))

    def __pow__(self, power, modulo=None):
        return mint(pow(self.__x, power, md))


md = 998244353


def main():
    n = II()
    aa = LI()
    sa = sum(aa)
    dp = [mint(0)] * (sa + 1)
    for i in range(1, sa + 1):
        dp[i] = ((i - 1) * dp[i - 1] + sa) * (n - 1) / (sa + 1 - i)

    for i in range(sa):
        dp[i + 1] += dp[i]

    ans = -(n - 1) * dp[-1]
    for a in aa:
        ans += dp[sa] - dp[a]
    print(ans / n)


main()
