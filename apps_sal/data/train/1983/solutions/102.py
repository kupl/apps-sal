class ProductOfNumbers:

    def __init__(self):
        self.vec = []
        # self.runningProd = []

    def add(self, num: int) -> None:

        if num == 0:
            self.vec = []

        else:
            if self.vec:
                curr = self.vec[-1]
            else:
                curr = 1

            self.vec.append(num * curr)

    def getProduct(self, k: int) -> int:

        if len(self.vec) < k:
            return 0
        elif len(self.vec) == k:
            return self.vec[-1]
        else:
            return self.vec[-1] // self.vec[-k - 1]

        # outval = self.vec[-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
