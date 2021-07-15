
import math
class ProductOfNumbers:

    def __init__(self):
        self.a = []

    def add(self, num: int) -> None:
        self.a.append(num)
        

    def getProduct(self, k: int) -> int:
        return math.prod(self.a[-k:])
        
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

