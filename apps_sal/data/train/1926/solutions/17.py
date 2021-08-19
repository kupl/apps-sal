class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        for k in range(int(math.sqrt(num + 2)), 0, -1):
            for x in (num + 1, num + 2):
                if not x % k:
                    return (x // k, k)
