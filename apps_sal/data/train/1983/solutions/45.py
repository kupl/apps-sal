class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.latest_zero_position = None

    def add(self, num: int) -> None:
        if num == 0:
            self.latest_zero_position = len(self.products)
            num = 1
        self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if self.latest_zero_position != None:
            if self.latest_zero_position >= len(self.products) - k:
                return 0

        return self.products[-1] // self.products[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
