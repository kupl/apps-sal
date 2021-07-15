from functools import lru_cache, reduce
from operator import mul
class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.size = 0

    def add(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1
        self.getProduct.cache_clear()
    
    @lru_cache
    def getProduct(self, k: int) -> int:
        return reduce(mul,self.arr[self.size-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

