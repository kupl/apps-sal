class ProductOfNumbers:
    
    prod_list = []
    
    def __init__(self):
        pass

    def add(self, num: int) -> None:
        if num == 0:
            self.prod_list = []
        else:
            if len(self.prod_list) == 0:
                self.prod_list.append(num)
            else:
                new_prod = self.prod_list[-1]*num
                self.prod_list.append(new_prod)

    def getProduct(self, k: int) -> int:
        if len(self.prod_list) == 0:
            return 0
        
        if k > len(self.prod_list):
            return 0
        elif k == len(self.prod_list):
            return self.prod_list[-1]
        else:
            if self.prod_list[-k] == 0:
                return 0
            else:
                return self.prod_list[-1]//self.prod_list[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

