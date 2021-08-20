class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        vals = (num + 1, num + 2)
        for lo in itertools.count(int((num + 2) ** 0.5), -1):
            for val in vals:
                if val % lo == 0:
                    return (lo, val // lo)
