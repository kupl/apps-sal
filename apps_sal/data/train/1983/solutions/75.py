class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.product = [1]
        else:

            self.product.append(self.product[-1] * num)
      # [1 , 3, 4, .... k, 3 , 2, 1]

    def getProduct(self, k: int) -> int:
        n = len(self.product) - 1

        return self.product[n] // self.product[n - k] if k <= n else 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
