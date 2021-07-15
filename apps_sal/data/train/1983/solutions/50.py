class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.n = 0
        self.zero = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.product.append(0)
            self.zero = self.n
        else:
            if self.n == 0 or self.product[-1] == 0:
                self.product.append(num)
            else:
                self.product.append(num*self.product[-1])
        self.n += 1
        # print(self.product)

    def getProduct(self, k: int) -> int:
        if self.zero >= self.n-k: return 0
        if k == self.n or self.n-k-1 == self.zero:
            return self.product[-1]
        return self.product[-1]//self.product[self.n-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

