class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        x = int((num + 2) ** 0.5)
        best = [float('inf'), -float('inf')]
        for y in range(x, 0, -1):
            for z in (num + 1, num + 2):
                if z % y == 0:
                    if abs(y - z // y) < abs(best[0] - best[1]):
                        best = [y, z // y]
        return best
