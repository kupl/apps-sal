class Solution:
    def closestDivisors(self, x: int) -> List[int]:
        for a in range(int((x+2) ** 0.5), 0, -1):
            if (x + 1) % a == 0:
                return [a, (x + 1) // a]
            if (x + 2) % a == 0:
                return [a, (x + 2) // a]
        
        return []
