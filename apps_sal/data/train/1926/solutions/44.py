class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        (fpairs1, fpairs2) = ([], [])
        for i in range(1, int((num + 1) ** 0.5) + 1):
            if (num + 1) % i == 0:
                fpairs1.append([i, int((num + 1) / i)])
        for i in range(1, int((num + 2) ** 0.5) + 1):
            if (num + 2) % i == 0:
                fpairs2.append([i, int((num + 2) / i)])
        return fpairs1[-1] if abs(fpairs1[-1][0] - fpairs1[-1][1]) < abs(fpairs2[-1][0] - fpairs2[-1][1]) else fpairs2[-1]
