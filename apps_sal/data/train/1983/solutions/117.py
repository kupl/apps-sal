class ProductOfNumbers:

    def __init__(self):
        self.last = -1
        self.pre = [1] * 500000
        self.n = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.pre[self.n] = 1
            self.last = self.n
        elif self.n == 0:
            self.pre[self.n] = num
        else:
            self.pre[self.n] = self.pre[self.n - 1] * num
        self.n += 1

    def getProduct(self, k: int) -> int:
        l = self.n - k
        if self.last >= l:
            return 0
        return self.pre[self.n - 1] // self.pre[l - 1]
