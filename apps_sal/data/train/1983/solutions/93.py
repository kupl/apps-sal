class ProductOfNumbers:

    def __init__(self):
        self.products = []
        

    def add(self, num: int) -> None:
        
        if num == 0:
            self.products = []    
        else:
            self.products.append(num if not len(self.products) else self.products[-1] * num)
           
    def getProduct(self, k: int) -> int:
        if k > len(self.products):
            return 0
        elif k == len(self.products):
            return self.products[-1]
        else:
            return self.products[-1] // self.products[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

