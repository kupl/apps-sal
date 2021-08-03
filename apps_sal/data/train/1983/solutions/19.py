class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        self.list = []
        self.zero = False

    def add(self, num: int):
        self.list.append(num)
        if not num:
            self.zero = True
            self.product.append(0)
        else:
            if self.zero:
                self.product.append(num)
                self.zero = False
            else:
                self.product.append(num * self.product[-1])

    def getProduct(self, k: int) -> int:
        # print(\"product\", self.product)
        # print(\"list\", self.list)
        # print(\"k =\", k)
        if not all(self.product[-k:-1]):
            return 0
        else:
            if not self.product[-k - 1]:
                return int(self.product[-1])
            else:
                return int(self.product[-1] / self.product[-k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
