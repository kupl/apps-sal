class ProductOfNumbers:    
    def __init__(self):
        self.lisst = []

    def add(self, num: int) -> None:
        self.lisst += [num]

    def getProduct(self, k: int) -> int:
        return prod(self.lisst[len(self.lisst) - k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

