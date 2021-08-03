class ProductOfNumbers:

    def __init__(self):
        self.products = []
        self.zero_point = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.products.append(0)
            self.zero_point = len(self.products)
        elif not self.products or self.products[-1] == 0:
            self.products.append(num)
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if len(self.products) - self.zero_point < k:
            ret = 0
        elif len(self.products) - self.zero_point == k or len(self.products) == k:
            ret = self.products[-1]
        else:
            ret = self.products[-1] // self.products[-k - 1]
        return ret

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
