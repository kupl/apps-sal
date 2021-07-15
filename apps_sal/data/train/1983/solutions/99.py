class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.products = []
        self.lastZero = -1

    def add(self, num: int) -> None:
        self.nums.append(num)
        if(num == 0):
            self.lastZero = len(self.nums)
            self.products.append(0)
        elif len(self.products) == 0:
            self.products.append(num)
        else:
            if self.products[-1] == 0:
                self.products.append(num)
            else:
                self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.lastZero != -1 and k == len(self.nums):
            return 0
        if len(self.nums) - k >= self.lastZero:
            divisor = 1
            if k + 1 <= len(self.nums) and self.products[-k - 1] != 0:
                divisor = self.products[-k - 1]
            return int(self.products[-1]/divisor)
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

