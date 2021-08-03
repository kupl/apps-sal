class ProductOfNumbers:

    def __init__(self):
        self.product_list = []

    def add(self, num: int) -> None:
        self.product_list.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.product_list[-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
