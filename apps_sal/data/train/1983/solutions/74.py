class ProductOfNumbers:

    def __init__(self):
        self.numlist = []
        self.cumprod = []
        self.zeros = []

    def add(self, num: int) -> None:
        self.numlist.append(num)
        if self.cumprod == [] or self.cumprod[-1] == 0:
            self.cumprod.append(num)
        else:
            new = self.cumprod[-1] * num
            self.cumprod.append(new)
        if num == 0:
            self.zeros.append(len(self.cumprod) - 1)

    def getProduct(self, k: int) -> int:
        if self.zeros != [] and len(self.cumprod) - k <= self.zeros[-1]:
            return 0
        else:
            if k == len(self.cumprod):
                return self.cumprod[k - 1]
            else:
                ii = len(self.cumprod) - k
                return self.numlist[ii] * self.cumprod[-1] // self.cumprod[ii]
