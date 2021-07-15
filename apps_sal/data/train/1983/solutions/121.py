class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.cache = {}
        

    def add(self, num: int) -> None:
        self.nums.append(num)
        

    def getProduct(self, k: int) -> int:
        tkey = (len(self.nums),k)
        prod = self.cache.get(tkey, None)
        if not prod:
            prod = 1 
            for n in self.nums[-k:]:
                if n == 0:
                    self.cache[tkey] = 0
                    return 0
                if n == 1:
                    continue
                prod *= n
            self.cache[tkey] = prod
        return prod
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

