def findDivisors(n):
    res = []
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            res.append([i, n // i])
        i = i + 1
    return res


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        A = findDivisors(num + 1)
        B = findDivisors(num + 2)

        return A[-1] if abs(A[-1][0] - A[-1][1]) < abs(B[-1][0] - B[-1][1]) else B[-1]
