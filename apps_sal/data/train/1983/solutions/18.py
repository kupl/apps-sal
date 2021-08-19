class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.product = []

    def add(self, num: int) -> None:
        self.data.append(num)
        if len(self.data) % 10 == 0:
            self.product.append(self.getLastTenProduct())

    def getLastTenProduct(self) -> int:
        res = 1
        for i in range(len(self.data) - 1, len(self.data) - 11, -1):
            res *= self.data[i]
        return res

    def getProduct(self, k: int) -> int:
        remain = k % 10
        tenth = k // 10
        res = 1
        for i in range(len(self.product) - 1, len(self.product) - tenth - 1, -1):
            res *= self.product[i]

        for i in range(
            len(self.data) - tenth * 10 - 1,
            len(self.data) - tenth * 10 - remain - 1,
            -1
        ):
            res *= self.data[i]
        return res


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
