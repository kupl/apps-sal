class ProductOfNumbers:

    def __init__(self):
        self.cum_prod = []
        self.arr = []
        self.n = 0
        self.zero_flags = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_flags.append(self.n)
        if len(self.arr) > 0:
            if self.arr[-1] == 0:
                self.cum_prod.append(num)
            else:
                self.cum_prod.append(num * self.cum_prod[-1])
        else:
            self.cum_prod.append(num)
        self.arr.append(num)
        self.n += 1

    def getProduct(self, k: int) -> int:
        if len(self.zero_flags) > 0 and max(self.zero_flags) > self.n-k-1:
            return 0
        if len(self.cum_prod) == k:
            return self.cum_prod[-1]
        den = self.cum_prod[self.n-k-1]
        if den == 0:
            return self.cum_prod[-1]
        return self.cum_prod[-1]//den


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

