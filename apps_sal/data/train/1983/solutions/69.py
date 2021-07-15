class ProductOfNumbers:

    def __init__(self):
        self.numbers = []
        self.history = {}

    def add(self, num: int) -> None:
        self.numbers.append(num)
        self.history = {}
        
    def getProduct(self, k: int) -> int:     
        if k not in self.history:
            self.history[k] = (self.numbers[len(self.numbers)-k] * self.getProduct(k-1) if self.numbers[len(self.numbers)-k] else 0 ) if k else 1
        
        return self.history[k]  

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

