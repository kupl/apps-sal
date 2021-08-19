class ProductOfNumbers:

    def __init__(self):
        self.dp = [1]
        self.lastZero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.lastZero = len(self.dp)
            num = 1
        self.dp.append(num * self.dp[-1])

    def getProduct(self, k: int) -> int:
        if len(self.dp) - k <= self.lastZero:
            return 0
        if len(self.dp) - k - 1 < 0:
            return self.dp[-1]
        return self.dp[-1] // self.dp[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
