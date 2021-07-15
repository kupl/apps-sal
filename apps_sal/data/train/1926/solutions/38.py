class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        ans = num + 1
        val = None
        for i in range(1, ceil(sqrt(num+3))):
            if (num + 1) % i == 0:
                j = (num + 1) // i
                if abs(i-j) <= ans:
                    ans = abs(i-j)
                    val = [i, j]
            if (num + 2) % i == 0:
                j = (num + 2) // i
                if abs(i-j) <= ans:
                    ans = abs(i-j)
                    val = [i, j]
        return val

