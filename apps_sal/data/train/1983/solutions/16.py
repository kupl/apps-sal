class ProductOfNumbers:

    def __init__(self):
        self.l = []
        self.cache = {}

    def add(self, num: int) -> None:
        self.l.append(num)
        self.cache = {}

    def getProduct(self, k: int) -> int:
        if k in self.cache:
            return self.cache[k]
        elif k - 1 in self.cache:
            return self.cache[k - 1] * self.l[-k]
        else:
            prod = 1
            for num in self.l[-k:]:
                prod *= num
            self.cache[k] = prod
        return prod
