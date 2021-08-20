class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.product_cache = {}

    def add(self, num: int) -> None:
        self.data.append(num)

    def getProduct(self, k: int) -> int:
        product = self.product_cache.get((len(self.data) - k, len(self.data) - 1))
        if product is not None:
            return product
        product = 1
        for i in self.data[-k:]:
            product = product * i
        self.product_cache[len(self.data) - k, len(self.data) - 1] = product
        return product
