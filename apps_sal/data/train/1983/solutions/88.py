class ProductOfNumbers:

    def __init__(self):
        self.A = [1]

    def add(self, num: int) -> None:
        if not num:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * num)

    def getProduct(self, k: int) -> int:

        if k >= len(self.A):
            return 0
        return self.A[-1] // self.A[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
