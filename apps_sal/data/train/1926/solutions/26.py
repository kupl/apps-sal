class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        (num1, num2) = (num + 1, num + 2)
        i = int(math.sqrt(num1))
        m = int(math.sqrt(num2))
        while i > 0:
            if num1 % i == 0:
                j = num1 // i
                res1 = j - i
                break
            else:
                i -= 1
        while m > 0:
            if num2 % m == 0:
                n = num2 // m
                res2 = n - m
                break
            else:
                m -= 1
        if res1 < res2:
            return [i, j]
        else:
            return [m, n]
