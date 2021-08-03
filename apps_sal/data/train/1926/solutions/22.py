class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        return min([divs(num + 1), divs(num + 2)], key=lambda t: t[1] - t[0])


def divs(n):
    ans = []
    for i in range(1, 1 + int(n**.5)):
        if n % i == 0:
            ans = [i, n // i]
    return ans
