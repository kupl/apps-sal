class Solution:

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = []
        max_digits = 9
        for depth in range(2, max_digits + 1):
            nums += self.genNum(max_digits, depth)
        return [n for n in nums if n >= low and n <= high]

    def genNum(self, max_digits, depth):
        result = []
        for startDigit in range(1, max_digits - depth + 2):
            num = startDigit
            for lvl in range(depth - 1):
                num = num * 10 + num % 10 + 1
            result.append(num)
        return result
