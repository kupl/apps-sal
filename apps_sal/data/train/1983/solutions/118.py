from sortedcontainers import SortedList


class ProductOfNumbers:

    def __init__(self):
        self.arr = list()
        self.prod = list()
        self.zeros = SortedList()

    def add(self, n: int) -> None:
        num = 0
        if n == 0:
            num = 1
            self.zeros.add(len(self.prod))
        else:
            num = n

        self.arr.append(num)
        if len(self.prod) == 0:
            self.prod.append(num)
        else:
            self.prod.append(num * self.prod[-1])

    def getProduct(self, k: int) -> int:

        idx = len(self.prod) - k

        if self.zeros.bisect_left(idx) != len(self.zeros):
            return 0

        if k == len(self.prod):
            return self.prod[-1]
        else:
            return int(self.prod[-1] / self.prod[len(self.prod) - k - 1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
