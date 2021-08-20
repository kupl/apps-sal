class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        diff = num + 1
        for i in range(1, int((num + 1) ** 0.5) + 1):
            if (num + 1) % i == 0:
                (num1_, num1__) = (i, (num + 1) // i)
        diff = num + 2
        for i in range(1, int((num + 2) ** 0.5) + 1):
            if (num + 2) % i == 0:
                (num2_, num2__) = (i, (num + 2) // i)
        diff1 = num1__ - num1_
        diff2 = num2__ - num2_
        return [num1_, num1__] if diff1 < diff2 else [num2_, num2__]
