class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.product = []
        self.last_zero = -1

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.product = [0] * len(self.product)
            self.last_zero = len(self.nums) - 1
        else:
            if num != 1:
                for i in range(len(self.product) - 1, self.last_zero, -1):
                    self.product[i] *= num
        self.product.append(num)

    def getProduct(self, k: int) -> int:
        if len(self.product) < k:
            return None
        return self.product[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
