class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        x, y = self.get_factors(num+1)
        z, t = self.get_factors(num+2)
        return [x, y] if abs(x-y) <= abs(z-t) else [z, t]
    
    def get_factors(self, n):
        y = n
        for x in range(1, int(sqrt(n))+1):
            # y = int(n/x) if (n/float(x)).is_integer() else y
            # alternatively, using mod is faster than direct division:
            y = int(n/x) if n % x == 0 else y

        return int(n/y), y
