import numpy as np

class ProductOfNumbers:

    def __init__(self):
        self.data = [1]
 
    def add(self, num: int) -> None:
        if num == 0:
            self.data = [1]
        else:
            self.data.append(num * self.data[-1])
 
    def getProduct(self, k: int) -> int:
        if k >= len(self.data):
            return 0
        return self.data[-1] // self.data[ - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

