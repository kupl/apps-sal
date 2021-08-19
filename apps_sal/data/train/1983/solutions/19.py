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
        elif self.zero:
            self.product.append(num)
            self.zero = False
        else:
            self.product.append(num * self.product[-1])

    def getProduct(self, k: int) -> int:
        if not all(self.product[-k:-1]):
            return 0
        elif not self.product[-k - 1]:
            return int(self.product[-1])
        else:
            return int(self.product[-1] / self.product[-k - 1])
