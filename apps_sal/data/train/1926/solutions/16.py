class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def maxFactor(n):
            if n < 3:
                return n
            for i in range(int(math.sqrt(n)), 0, -1):
                if not n % i:
                    return i
            return 1
        res = [] 
        for n in [num + 1, num + 2]:
            a = maxFactor(n)
            b = n // a
            res.append((abs(a - b), [a, b]))
        return min(res, key = lambda x:x[0])[1]
