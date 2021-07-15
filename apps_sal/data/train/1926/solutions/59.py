class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def compute(n):
            diff = float(\"inf\")
            res = []
            for i in range(1, 1+int(n**0.5)):
                if n % i == 0:
                    if abs(n//i - i) < diff:
                        diff = abs(n//i - i)
                        res = [n//i, i]
            return [diff, res]
        d1, r1 = compute(num+1)
        d2, r2 = compute(num+2)
        return r1 if d1 < d2 else r2
