class ProductOfNumbers:

    def __init__(self):
        self.stack = []
        self.acc = []

    def add(self, num: int) -> None:
        if num == 0:
            self.stack = []
            return
        if self.stack:
            self.stack.append(self.stack[-1] * num)
        else:
            self.stack.append(num)

    def getProduct(self, k: int) -> int:
        if k > len(self.stack):
            return 0
        if k == len(self.stack):
            return self.stack[-1]
        return self.stack[-1] // self.stack[-k - 1]
