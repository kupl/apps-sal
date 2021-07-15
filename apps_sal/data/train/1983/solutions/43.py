class ProductOfNumbers:

    def __init__(self):
        self.nums = [1]
        self.prod = [1]
        self.pz_list = [-1]
        self.prev_zero = -1

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num > 0:
            self.pz_list.append(self.prev_zero)
            if self.prod[-1] != 0:
                self.prod.append(self.prod[-1] * num)
            else:
                self.prod.append(num)
        else:
            self.prev_zero = len(self.nums) - 1
            self.pz_list.append(self.prev_zero)
            self.prod.append(1)
            
    def getProduct(self, k: int) -> int:
        if len(self.nums) - 1 - self.pz_list[-1] < k:
            return 0
        else:
            return self.prod[-1] // self.prod[-1 * k -1] 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

