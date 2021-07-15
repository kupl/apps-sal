import math
class ProductOfNumbers:

    def __init__(self):
        self.usable_array = []

    def add(self, num: int) -> None:
        self.usable_array.append(num)

    def getProduct(self, k: int) -> int:
        if type(k) != int:
            self.usable_array = ProductOfNumbers()
        #product = 1
        product = math.prod(self.usable_array[-k:])
        return product


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

