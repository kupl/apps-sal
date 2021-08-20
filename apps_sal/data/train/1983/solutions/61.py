from functools import reduce


class ProductOfNumbers:

    def __init__(self):
        self.list = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.list = [1]
        else:
            result = self.list[-1] * num
            self.list.append(result)

    def getProduct2(self, k: int) -> int:
        return reduce(lambda x, y: x * y, self.list[-k:])

    def getProduct(self, k: int) -> int:
        if len(self.list) <= k:
            return 0
        ind = -1 - k
        if self.list[ind] == 0:
            return 0
        else:
            return self.list[-1] // self.list[ind]
