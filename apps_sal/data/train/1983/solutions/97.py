import math


class ProductOfNumbers:

    def __init__(self):
        self.prefixes_products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixes_products = []
            self.prev = 0
            return

        if not self.prefixes_products:
            self.prefixes_products.append(num)
        else:
            self.prefixes_products.append(num * self.prev)

        self.prev = self.prefixes_products[-1]

    def getProduct(self, k: int) -> int:
        if len(self.prefixes_products) == k:
            return self.prev
        if len(self.prefixes_products) < k:
            return 0

        return self.prev // self.prefixes_products[len(self.prefixes_products) - k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
