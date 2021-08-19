class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        self.arr = [1] if num == 0 else self.arr + [num * self.arr[-1]]

    def getProduct(self, k: int) -> int:
        return 0 if len(self.arr) <= k else int(self.arr[-1] / self.arr[-k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
