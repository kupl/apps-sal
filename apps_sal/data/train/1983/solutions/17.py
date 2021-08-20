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
        for i in self.listOfProds[-1 * k:]:
            outProd = outProd * i
        self.results[k] = outProd
        return outProd
