class ProductOfNumbers:

    def __init__(self):
        self.last = -1
        self.pre = [1] * 500000
        self.n = 0
        
    def add(self, num: int) -> None:
        if num == 0:
            self.pre[self.n] = 1
            self.last = self.n
        else:
            if self.n == 0:
                self.pre[self.n] = num
            else:
                self.pre[self.n] = self.pre[self.n - 1] * num
        self.n += 1
        
    def getProduct(self, k: int) -> int:
        l = self.n - k
        if self.last >= l:
            return 0
        # print(self.n - 1, l, self.last)
        return self.pre[self.n - 1] // self.pre[l - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

