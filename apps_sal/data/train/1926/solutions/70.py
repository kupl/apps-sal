class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        cd1 = self.closestDivisorWithProduct(num + 1)
        cd2 = self.closestDivisorWithProduct(num + 2)
        if cd1 == None:
            return cd2
        elif cd2 == None:
            return cd1
        if abs(cd1[0] - cd1[1]) < abs(cd2[0] - cd2[1]):
            return cd1
        else:
            return cd2

    def closestDivisorWithProduct(self, num):
        divisors = [(i, num // i) for i in range(1, int(num ** 0.5) + 1) if num % i == 0]
        minPair = None
        minDiff = num
        for (a, b) in divisors:
            if a * b != num:
                continue
            if abs(a - b) < minDiff:
                minPair = (a, b)
                minDiff = abs(a - b)
        return minPair
