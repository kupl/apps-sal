import math


class ProductOfNumbers:

    def __init__(self):
        self.usable_array = []

    def add(self, num: int) -> None:
        self.usable_array.append(num)

    def getProduct(self, k: int) -> int:
        if type(k) != int:
            self.usable_array = ProductOfNumbers()
        product = math.prod(self.usable_array[-k:])
        return product
