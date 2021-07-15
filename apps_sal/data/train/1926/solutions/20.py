class Solution:
    def divizor(self, num):
        for i in range( int(math.sqrt(num)), 0, -1):
            n1 = num / i
            if n1.is_integer():
                return [int(n1), int(num / n1)]

    def closestDivisors(self, num: int) -> List[int]:
        r = []
        diff = None
        for i in [num + 1, num + 2]:
            d = self.divizor(i)
            if not d:
                continue
            abs_diff = abs(d[0] - d[1])
            if diff == None or abs_diff < diff:
                diff = abs_diff
                r = d
        return r

