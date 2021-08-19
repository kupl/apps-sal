class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.max_k = 0
        self.step = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.max_k = self.step
        else:
            self.products.append(self.products[-1] * num)
            self.step += 1

    def getProduct(self, k: int) -> int:
        if k > self.step - self.max_k:
            return 0
        return int(self.products[-1] / self.products[self.step - k])
