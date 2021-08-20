class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
        else:
            self.product.append(self.product[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.product) - 1
        return self.product[n] // self.product[n - k] if k <= n else 0
