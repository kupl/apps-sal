class ProductOfNumbers:

    def __init__(self):
        self.prods = []
        self.stamp = []
        

    def add(self, num: int) -> None:
        self.prods.append(num)
        self.stamp.append(1)
        
        [3, 0, 2, 5, 4]
        [1, 1, 1, 1, 1]
        

    def getProduct(self, k: int) -> int:
        if k <= 0:
            return 1
        
        index = len(self.prods) - k
        if self.stamp[index] == k:
            return self.prods[index]
        
        value = self.prods[index] * self.getProduct(k - self.stamp[index])
        
        self.stamp[index] = k
        self.prods[index] = value
        
        return value
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

