class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = []
            return
        if not self.arr:
            self.arr.append(num)
            return
        self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.arr):
            return 0
        if k == len(self.arr):
            return self.arr[-1]
        return self.arr[-1] // self.arr[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
