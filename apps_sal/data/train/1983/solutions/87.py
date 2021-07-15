class ProductOfNumbers:

    def __init__(self):
        self.z = []
        self.s = 1
        self.l = []
        self.m = [1]
        self.ind = -1

    def add(self, num: int) -> None:
        self.ind += 1
        self.l.append(num)
        self.s *= num
        self.m.append(self.s)
        if num == 0:
            self.z.append(self.ind)
            self.s = 1
            self.m[-1] = 1
        # print(num, self.l,self.m,self.s)

    def getProduct(self, k: int) -> int:
        if len(self.z) and self.z[-1] > self.ind - k:
            return 0
        else:
            # print(k,self.z[-1],self.ind)
            # print(self.m)
            return int(self.m[-1] // self.m[-k-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

