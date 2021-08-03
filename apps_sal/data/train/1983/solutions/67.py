class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.prod = [1]

    def add(self, num: int) -> None:
        self.data.append(num)
        if num != 0 and self.prod[-1] != 0:
            self.prod.append(self.prod[-1] * num)
        elif num == 0:
            self.prod = (len(self.prod)) * [0]
            self.prod.append(1)
            # elif self.prod[-1] == 0:
            #     self.prod.append(num)
        # elif num:
        #     self.prod.append(num)
        # else:
        #     self.prod.append(1)

    def getProduct(self, k: int) -> int:
        # print(self.prod)
        return self.prod[-1] // self.prod[-1 - k] if self.prod[-1 - k] else 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
