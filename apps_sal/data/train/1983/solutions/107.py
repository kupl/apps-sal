from collections import deque


class ProductOfNumbers:

    def __init__(self):
        self.running_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.running_products = [1]
        else:
            self.running_products.append(self.running_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.running_products) < k + 1:
            return 0
        return int(self.running_products[-1] / self.running_products[-k - 1])
