class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def helper(k):
            for i in range(int(math.sqrt(k)), 0, -1):
                if k % i == 0:
                    return [i, k // i]
        return sorted([helper(num + 1), helper(num + 2)], key=lambda c: abs(c[0] - c[1]))[0]
