class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.cache = {}
        

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.cache = {}
        

    def getProduct(self, k: int) -> int:
        if k in self.cache:
            return self.cache[k]
        n = self.nums[-k:]
        ret = 1
        for e in n:
            ret *= e
        self.cache[k] = ret
        return ret
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

