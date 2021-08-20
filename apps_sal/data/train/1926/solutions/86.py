import math


class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2
        divisor = []
        divisor = self.find_divisors(num1, 1000000001, divisor)
        divisor = self.find_divisors(num2, abs(divisor[0] - divisor[1]), divisor)
        return divisor

    def find_divisors(self, num, difference, divisors):
        i = 1
        while i <= math.sqrt(num):
            if num % i == 0:
                second = num // i
                diff = abs(second - i)
                if diff < difference:
                    divisors = [i, second]
            i += 1
        return divisors
