class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.zeros = []
        self.product = 1
        self.allProducts = {}  # index -> product at that index

    def add(self, num: int) -> None:
        if num == 0:
            self.zeros.append(len(self.nums))
        else:
            self.product *= num

        self.nums.append(num)
        self.allProducts[len(self.nums) - 1] = self.product

    def getProduct(self, k: int) -> int:
        for i in self.zeros:
            if len(self.nums) - k <= i <= len(self.nums) - 1:
                return 0
        if k == len(self.nums):
            return self.product
        return int(self.product / self.allProducts[len(self.nums) - 1 - k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
