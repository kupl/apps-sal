class ProductOfNumbers:

    def __init__(self):
        self.k1 = []
        self.mul = 1

    def add(self, num: int) -> None:
        if num != 0:
            self.mul *= num
            self.k1.append(self.mul)
        else:
            self.mul = 1
            self.k1 = []

    def getProduct(self, k: int) -> int:
        if k > len(self.k1):
            return 0
        elif k == len(self.k1):
            return self.k1[-1]
        else:
            return self.k1[-1] // self.k1[-1 - k]
