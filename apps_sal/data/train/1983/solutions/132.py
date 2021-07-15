import numpy as np

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prods = np.array([])
        

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.prods = self.prods * num
        self.prods = np.append(self.prods, num)

    def getProduct(self, k: int) -> int:
        return int(self.prods[-k])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

