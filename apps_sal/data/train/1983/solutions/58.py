class ProductOfNumbers:

    def __init__(self):
        self.runningProduct = []
        self.zeroStack = []
        self.addedZero = False

    def add(self, num: int) -> None:
        if num == 0:
            self.runningProduct.append(num)
            self.addedZero = True
            self.zeroStack.append(len(self.runningProduct) - 1)
        else:
            if self.addedZero or len(self.runningProduct) == 0:
                self.runningProduct.append(num)
            else:
                currentProduct = num * self.runningProduct[-1]
                self.runningProduct.append(currentProduct)
            self.addedZero = False

    def getProduct(self, k: int) -> int:
        totalIndex = len(self.runningProduct) - 1
        if self.zeroStack and self.zeroStack[-1] > (totalIndex - k):
            return 0
        elif (totalIndex - k) == -1 or self.runningProduct[totalIndex - k] == 0:
            return int(self.runningProduct[-1])
        else:
            return int(self.runningProduct[-1] / self.runningProduct[totalIndex - k])
