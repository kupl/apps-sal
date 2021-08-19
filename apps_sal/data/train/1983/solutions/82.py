class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        if not num:
            self.arr = []
        else:
            prev_prod = self.arr[-1] if self.arr else 1
            self.arr.append(num * prev_prod)
        return

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        elif len(self.arr) == k:
            return self.arr[-1]
        else:
            return self.arr[-1] // self.arr[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
