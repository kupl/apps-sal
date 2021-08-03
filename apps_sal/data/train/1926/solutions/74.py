import math


class Solution:
    def get_closest(self, num):
        for val in range(int(math.sqrt(num)), 0, -1):
            if not num % val:
                return [val, num // val]
        return [1, num]

    def closestDivisors(self, num: int) -> List[int]:
        temp1, temp2 = self.get_closest(num + 1), self.get_closest(num + 2)
        return temp1 if (abs(temp1[0] - temp1[1]) < abs(temp2[0] - temp2[1])) else temp2
