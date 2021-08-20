class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        result = [None, None]
        i = 1
        while i * i <= num + 2:
            if not (num + 1) % i:
                result = [i, (num + 1) // i]
            elif not (num + 2) % i:
                result = [i, (num + 2) // i]
            i += 1
        return result
