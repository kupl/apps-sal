class ProductOfNumbers:

    def __init__(self):
        self.array = []

    def add(self, num: int) -> None:
        if num == 0:
            self.array = []
        else:
            self.array.append(self.array[-1] * num if self.array else num)

    def getProduct(self, k: int) -> int:
        if len(self.array) < k:
            return 0
        if len(self.array) == k:
            return self.array[-1]
        return self.array[-1] // self.array[-k - 1]
