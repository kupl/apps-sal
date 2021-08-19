import numpy as np


class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prods = np.array([])

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.prods = (self.prods * num).astype(int)
        self.prods = np.append(self.prods, num)

    def getProduct(self, k: int) -> int:
        return self.prods[-k]
