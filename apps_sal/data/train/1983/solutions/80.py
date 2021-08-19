class ProductOfNumbers:

    def __init__(self):
        self.idx = 0
        self.pos2Prod = {}
        self.zeroPos = []
        self.currProd = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.zeroPos.append(self.idx)
            num = 1
        self.pos2Prod[self.idx] = self.currProd * num
        self.currProd = self.currProd * num
        self.idx += 1

    def getProduct(self, k: int) -> int:
        tailIdx = self.idx - 1
        headIdx = tailIdx - k
        if self.zeroPos and self.zeroPos[-1] > headIdx:
            return 0
        else:
            return self.pos2Prod[tailIdx] // (self.pos2Prod[headIdx] if headIdx >= 0 else 1)
