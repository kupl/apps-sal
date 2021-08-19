class Solution:

    def closestDivisors(self, num: int) -> List[int]:
        (num1, num2) = (num + 1, num + 2)

        def findDivisors(num):
            start = int(num ** 0.5)
            for i in range(start, 0, -1):
                if num % i == 0:
                    return [i, num // i]
        div1 = findDivisors(num1)
        div2 = findDivisors(num2)
        div_pairs = [div1, div2]
        res = min(div_pairs, key=lambda x: abs(x[0] - x[1]))
        return res
