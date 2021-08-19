class ProductOfNumbers:

    def __init__(self):
        self.prods = []
        self.zeros = []

    def add(self, num: int) -> None:
        zero = 1 if num == 0 else 0
        if not self.zeros:
            self.zeros.append(zero)
        else:
            self.zeros.append(self.zeros[-1] + zero)

        prod = max(1, num)
        if self.prods:
            self.prods.append(self.prods[-1] * prod)
        else:
            self.prods.append(prod)

    def getProduct(self, k: int) -> int:
        has_zero = False
        if len(self.zeros) == k:
            has_zero = self.zeros[-1] > 0
        else:
            has_zero = (self.zeros[-1] - self.zeros[-k - 1]) > 0
        if has_zero:
            return 0

        if len(self.prods) == k:
            return self.prods[-1]
        return self.prods[-1] // self.prods[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
