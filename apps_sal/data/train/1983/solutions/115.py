class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.tmp = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.products = []
            self.tmp = 1
        else:
            self.tmp *= num
            self.products.append(self.tmp)

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        elif len(self.products) == k:
            return self.products[-1]
        else:
            return self.products[-1] // self.products[-k - 1]
