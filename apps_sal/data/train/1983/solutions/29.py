class ProductOfNumbers:

    def __init__(self):
        self.arr = []

    def add(self, num: int) -> None:
        self.arr.append(num)

    def getProduct(self, k: int) -> int:
        # prod = 1
        # for num in self.arr[-k:]:
        #     if num == 0:
        #         return 0
        #     prod *= num
        # return prod
        return prod(self.arr[-k:])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

