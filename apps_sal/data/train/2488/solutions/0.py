class Solution:

    def findNumbers(self, nums: List[int]) -> int:

        def has_even_digits(number: int):
            if number < 10:
                return False
            elif number < 100:
                return True
            elif number < 1000:
                return False
            elif number < 10000:
                return True
            elif number < 100000:
                return False
            return True
        return sum([1 for num in nums if has_even_digits(num)])
