class ProductOfNumbers:

    def __init__(self):
        self.a = []

    def add(self, num: int) -> None:
        if num == 0:
            self.a = []
            return
        if not self.a:
            self.a.append(num)
            return
        self.a.append(self.a[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.a):
            return 0
        if k == len(self.a):
            return self.a[-1]
        return self.a[-1] // self.a[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
