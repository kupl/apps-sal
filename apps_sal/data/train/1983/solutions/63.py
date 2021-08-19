class ProductOfNumbers:

    def __init__(self):
        self.res = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.res = [1]
        else:
            self.res.append(self.res[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.res) <= k:
            return 0
        else:
            return self.res[-1] // self.res[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
