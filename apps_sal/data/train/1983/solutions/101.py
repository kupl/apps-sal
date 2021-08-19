from functools import reduce


class ProductOfNumbers:

    def __init__(self):
        self.running_product = []

    def add(self, num: int) -> None:
        if num == 0:
            self.running_product = []
        elif len(self.running_product) == 0:
            self.running_product.append(num)
        else:
            self.running_product.append(num * self.running_product[-1])
        return None

    def getProduct(self, k: int) -> int:
        if k > len(self.running_product):
            return 0
        elif k == len(self.running_product):
            return self.running_product[-1]
        else:
            return self.running_product[-1] // self.running_product[-k - 1]
