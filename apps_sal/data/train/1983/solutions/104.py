class ProductOfNumbers:

    def __init__(self):
        self.k1=[1]

    def add(self, num: int) -> None:
        if num!=0:
            self.k1.append(self.k1[-1]*num)
        else:
            self.k1=[1]

    def getProduct(self, k: int) -> int:
        if k>=len(self.k1):
            return 0
        return (self.k1[-1]//self.k1[-1-k])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

