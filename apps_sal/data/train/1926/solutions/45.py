class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        if num == 1:
            return [1, 2]
        if num == 2:
            return [2, 2]

        def getClose(val):
            yuh = set()
            for i in range(1, int(val ** 0.5) + 1):
                if val % i == 0 and ((val // i, i) not in yuh or (i, val // i) not in yuh):
                    yuh.add((val // i, i))
            m = 10 ** 9
            e = (-1, -1)
            for elem in yuh:
                if abs(elem[0] - elem[1]) < m:
                    e = elem
                    m = abs(elem[0] - elem[1])
            return e
        a = getClose(num + 1)
        b = getClose(num + 2)
        if abs(a[0] - a[1]) < abs(b[0] - b[1]):
            return list(a)
        return list(b)
