class ProductOfNumbers:

    def __init__(self):
        self.A = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.A = [1]
        else:
            self.A.append(self.A[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.A):
            return 0
        return self.A[-1] // self.A[-k - 1]
