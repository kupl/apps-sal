class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        result = []
        difference = float(\"inf\")
        for i in range(int((num + 2)**0.5) + 1, 0, -1):
            if (num + 1) % i == 0:
                a = i
                b = (num + 1) // a
                if abs(a - b) < difference:
                    difference = abs(a - b)
                    result = [a, b]
            if (num + 2) % i == 0:
                a = i
                b = (num + 2) // a
                if abs(a - b) < difference:
                    difference = abs(a - b)
                    result = [a, b]
        return result
