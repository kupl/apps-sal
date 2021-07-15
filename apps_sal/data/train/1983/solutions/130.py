import math
class ProductOfNumbers:

    def __init__(self):
        self.numbers = []
        self.cache = {}

    def add(self, num: int) -> None:
        self.numbers.append(num)
        self.cache = {}

    def getProduct(self, k: int) -> int:
        if k not in self.cache:
            self.cache[k] = math.prod(self.numbers[-k:])
        return self.cache[k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

