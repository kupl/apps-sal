class Solution:
    def closestDivisors(self, num: int) -> List[int]:

        num += 1
        for factor in range(int((num)**0.5), 0, -1):
            if num % factor == 0:
                num_1 = [factor, num // factor]
                break

        num += 1
        for factor in range(int((num)**0.5), 0, -1):
            if num % factor == 0:
                num_2 = [factor, num // factor]
                break

        return min(num_1, num_2, key=lambda x: abs(x[0] - x[1]))
