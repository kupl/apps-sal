class ProductOfNumbers:

    def __init__(self):
        self.hundreds = list()  
        self.nums = []
        self.hund_prods = 1
        self.hund_res = 0
        
        
    def add(self, num: int) -> None:
        self.nums.append(num)
        self.hund_prods *= num
        self.hund_res += 1
        if self.hund_res % 100 == 0:
            self.hundreds.append(self.hund_prods)
            self.hund_res = 0
            self.hund_prods = 1

    def prod(self, f, t):
        ret = 1
        for x in self.nums[f:t]:
            ret *= x
        return ret
    
    def getProduct(self, k: int) -> int:
        prod_tail = 1
        if k < 100 + self.hund_res:
            return self.prod(len(self.nums) - k, len(self.nums))
        else:
            account = self.hund_res
            p1 = self.prod(len(self.nums) - self.hund_res, len(self.nums))
            idx = -1
            while k - account > 100:
                account += 100
                p1 = p1 * self.hundreds[idx]
                idx = idx -1
            while account <= k:
                p1 = p1 * self.nums[-account]
                account += 1
            return p1
                
            
            
            
            
            


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

