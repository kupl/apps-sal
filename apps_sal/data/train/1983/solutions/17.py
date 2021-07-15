class ProductOfNumbers:

    def __init__(self):
        self.listOfProds = []
        self.results = {}
        
    def add(self, num: int) -> None:
        self.listOfProds.append(num)
        self.results = {}
        return None

    def getProduct(self, k: int) -> int:
        if k in self.results:
            return self.results[k]
        outProd = 1
        for i in self.listOfProds[-1*k:]:
            outProd = outProd * i
        self.results[k] = outProd
        return outProd


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

