class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [0] * len(self.prefix_prod) + [1]
        else:
            if self.prefix_prod[-1] == 0:
                self.prefix_prod.append(num)
            else:
                self.prefix_prod.append(self.prefix_prod[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_prod)
        if self.prefix_prod[n - k - 1] == 0:
            return 0
        else:
            return self.prefix_prod[n - 1] // self.prefix_prod[n - k - 1]
