class ProductOfNumbers:

    def __init__(self):
        self.prefixproducts = [1]

    def add(self, num: int) -> None:
        if num == 0:
            for i in range(len(self.prefixproducts)):
                self.prefixproducts[i] = 0
            self.prefixproducts.append(0)
        else:
            if self.prefixproducts[-1] != 0:
                self.prefixproducts.append(self.prefixproducts[-1] * num)
            else:
                self.prefixproducts.append(num)

    def getProduct(self, k: int) -> int:
        if self.prefixproducts[-(k + 1)] == 0:
            if self.prefixproducts[-k] == 0:
                return 0
            else:
                return self.prefixproducts[-1]
        else:
            return self.prefixproducts[-1] // self.prefixproducts[-(k + 1)]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
