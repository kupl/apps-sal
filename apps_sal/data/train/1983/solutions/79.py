import math


class ProductOfNumbers:

    def __init__(self):
        self.prefixes_products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prefixes_products.clear()
            return

        if not self.prefixes_products:
            self.prefixes_products.append(num)
        else:
            self.prefixes_products.append(num * self.prev)

        self.prev = self.prefixes_products[-1]

    def getProduct(self, k: int) -> int:
        if len(self.prefixes_products) == k:
            return self.prev
        elif len(self.prefixes_products) < k:
            return 0
        else:
            return self.prev // self.prefixes_products[len(self.prefixes_products) - k - 1]
