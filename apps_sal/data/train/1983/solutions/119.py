class ProductOfNumbers:
    def __init__(self):
        self.index = 0
        self.prefix = []
        self.zeroes = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroes.append(self.index)
            num = 1

        if not self.prefix:
            self.prefix.append(num)
        else:
            self.prefix.append(self.prefix[-1] * num)
        self.index += 1

    def getProduct(self, k: int) -> int:
        if self.zeroes and self.index - k <= self.zeroes[-1]:
            return 0
        elif k == len(self.prefix):
            return self.prefix[-1]
        else:
            return self.prefix[-1] // self.prefix[self.index - k - 1]
