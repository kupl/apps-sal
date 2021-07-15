class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]
        self.run = 1
        

    def add(self, num: int) -> None:
        if num != 0:
            self.run *= num
        else:
            n = len(self.arr)
            for i in range(n):
                self.arr[i] = 0
        self.arr.append(self.run)
        

    def getProduct(self, k: int) -> int:
        # print('for k ', k)
        # print('arr is ', self.arr)
        pre = 1
        n = len(self.arr)
        before = n - k - 1
        if before >= 0:
            pre = self.arr[before]
        
        if pre == 0:
            return 0
        return int(self.arr[-1] / pre)
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

