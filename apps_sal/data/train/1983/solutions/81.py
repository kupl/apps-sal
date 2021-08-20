class ProductOfNumbers:

    def __init__(self):
        self.prods = []
        self.currentProd = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.prods = []
            self.currentProd = 0
        else:
            if self.currentProd:
                self.currentProd *= num
            else:
                self.currentProd = num
            self.prods.append(self.currentProd)

    def getProduct(self, k: int) -> int:
        if len(self.prods) < k:
            return 0
        elif len(self.prods) == k:
            return int(self.currentProd)
        else:
            return int(self.currentProd / self.prods[-k - 1])
