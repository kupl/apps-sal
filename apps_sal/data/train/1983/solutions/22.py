from functools import reduce
from math import prod


class ProductOfNumbers:

    def __init__(self):
        self.nums = list()

    def add(self, num: int) -> None:
        self.nums.append(num)
        return
        if not self.nums:
            self.nums.append(num)
            return
        last_number = self.nums[-1] * num
        self.nums.append(last_number)

    def getProduct(self, k: int) -> int:
        last_k_nums = self.nums[-1 * k:]
        return prod(last_k_nums)
