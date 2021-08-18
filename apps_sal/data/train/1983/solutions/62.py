class ProductOfNumbers:

    def __init__(self):
        self.lst = []
        self.running = []
        self.last0index = -1
        self.size = 0

    def add(self, num: int) -> None:
        self.size += 1
        if not self.lst and num != 0:
            self.running.append(num)
        elif num == 0:
            self.running.append(1)
        elif self.lst[-1] == 0:
            self.running.append(num)
        else:
            self.running.append(num * self.running[-1])
        self.lst.append(num)

        if num == 0:
            self.last0index = self.size

    def getProduct(self, k: int) -> int:
        if self.size == 1:
            return self.lst[0]
        if k > self.size:
            return -1
        if self.size - k < self.last0index:
            return 0
        if self.size == k:
            return self.running[-1]

        return int(self.running[-1] / self.running[self.size - k - 1])
