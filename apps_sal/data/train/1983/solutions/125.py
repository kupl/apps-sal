class ProductOfNumbers:

    def __init__(self):
        self.array = []
        self.product = []

    def add(self, num: int) -> None:
        self.array.append(num)
        if len(self.product) > 0:
            i = 0
            if num == 0:
                self.product = [0] * len(self.product)
            else:
                while num != 1 and i < len(self.product) and self.product[i] != 0:
                    self.product[i] *= num
                    i += 1
            self.product.insert(0, num)
        elif len(self.product) == 0:
            self.product.append(num)

        
    def getProduct(self, k: int) -> int:
        return self.product[k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

