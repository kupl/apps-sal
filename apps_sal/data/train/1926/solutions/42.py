class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        n1 = {}
        n2 = {}
        n1[tuple([1, num + 1])] = abs(num + 1 - 1)
        for i in range(2, int(sqrt(num + 1)) + 1):
            if (num + 1) % i == 0:
                n1[tuple([i, int((num + 1) / i)])] = abs(int((num + 1) / i) - i)
        n2[tuple([1, num + 2])] = abs(num + 2 - 1)
        for i in range(2, int(sqrt(num + 2)) + 1):
            if (num + 2) % i == 0:
                n2[tuple([i, int((num + 2) / i)])] = abs(int((num + 2) / i) - i)
        r1 = sorted(n1.items(), key=lambda x: x[1])
        r2 = sorted(n2.items(), key=lambda x: x[1])
        if r1[0][1] < r2[0][1]:
            return list(r1[0][0])
        return list(r2[0][0])
