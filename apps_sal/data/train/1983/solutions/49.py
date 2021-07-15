class ProductOfNumbers:

    def __init__(self):
        self.products = [1]
        self.last_zero = -40001
        
    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = len(self.products) - 1
        if not self.products:
            self.products.append(num)
        else:
            self.products.append(self.products[-1] * max(1,num))
        

    def getProduct(self, k: int) -> int:
        if self.last_zero >= len(self.products) - k - 1:
            return 0
        result = int(self.products[-1]/self.products[len(self.products) - k - 1])
        return result

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

