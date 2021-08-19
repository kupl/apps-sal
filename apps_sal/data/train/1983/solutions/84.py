class ProductOfNumbers:

    def __init__(self):
        self.cur = 0
        self.prod = [1]
        self.last_zero = -1

    def add(self, num: int) -> None:
        if num != 0:
            self.prod.append(self.prod[-1] * num)
        else:
            self.prod.append(self.prod[-1])
            self.last_zero = self.cur
        self.cur += 1

    def getProduct(self, k: int) -> int:
        if self.cur - k > self.last_zero:
            return int(self.prod[-1] / self.prod[-k - 1])
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
