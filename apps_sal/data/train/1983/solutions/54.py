class ProductOfNumbers:

    def __init__(self):
        self.d = {}
        self.nulls = []
        self.index = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.nulls.append(self.index)
            num = 1

        if self.index == 0:
            self.d[self.index] = num
        else:
            self.d[self.index] = self.d[self.index - 1] * num

        self.index += 1

    def getProduct(self, k: int) -> int:

        if self.nulls and self.nulls[-1] > self.index - k - 1:
            return 0
        if self.index - k == 0:
            return self.d[self.index - 1]

        return self.d[self.index - 1] // self.d[self.index - k - 1]
