class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.zeroes = []
        self.index = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroes.append(self.index)
            self.index += 1
            self.products.append(self.products[-1])
        else:
            self.products.append(self.products[-1] * num)
            self.index += 1

    def getProduct(self, k: int) -> int:
        if self.zeroes and self.zeroes[-1] >= self.index - k:
            return 0
        else:
            return int(self.products[-1] / self.products[-(k + 1)])
