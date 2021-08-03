class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        # for num
        a = floor((num + 2)**0.5)
        n1 = None
        while a > 0:
            n = 0
            a2 = a**2
            if mod(num + 1 - a2, a) == 0:
                return [a, a + int((num + 1 - a2) / a)]
            if mod(num + 2 - a2, a) == 0:
                return [a, a + int((num + 2 - a2) / a)]
            # print(a,n1)
            a -= 1
