class ProductOfNumbers:

    def __init__(self):
        self.store = []

    def add(self, num: int) -> None:
        self.store.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.store[-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
