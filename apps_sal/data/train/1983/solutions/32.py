class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.n = 0

    def add(self, num: int) -> None:
        if num == 0:
            i = self.n-1
            self.product.append(0)
            while(i >= 0 and self.product[i] != 0):
                self.product[i] = 0
                i -= 1
        else:
            if self.n == 0 or self.product[-1] == 0:
                self.product.append(num)
            else:
                self.product.append(num*self.product[-1])
        self.n += 1
        # print(self.product)

    def getProduct(self, k: int) -> int:
        if k == self.n:
            if self.product[0] == 0: return 0
            else: return self.product[-1]

        if self.product[self.n-k] == 0:
            return 0
        elif self.product[self.n-k-1] == 0:
            return self.product[-1]
        else:
            return self.product[-1]//self.product[self.n-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

