class ProductOfNumbers:

    def __init__(self):
        self.length = 0
        self.prefix = [1]
        self.zeroPosition = []

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroPosition.append(self.length)
            self.prefix.append(self.prefix[-1])
        else:
            self.prefix.append(self.prefix[-1] * num)
        self.length += 1

    def getProduct(self, k: int) -> int:
        for p in self.zeroPosition:
            if self.length - k <= p <= self.length - 1:
                return 0
        return int(self.prefix[-1] / self.prefix[len(self.prefix) - k - 1])
