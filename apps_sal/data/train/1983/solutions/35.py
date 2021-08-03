import math


class ProductOfNumbers:

    def __init__(self):
        self.numList = []

    def add(self, num: int) -> None:
        self.numList.append(num)

    def getProduct(self, k: int) -> int:
        prodList = self.numList[(-1 * k):]

        # prod=1
        # length=len(self.numList)
        # for i in range(length-k, length):
        #    prod = prod * self.numList[i]

        return math.prod(prodList)


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
