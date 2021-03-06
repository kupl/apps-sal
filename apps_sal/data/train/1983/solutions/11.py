class ProductOfNumbers:

    def __init__(self):
        self.array = [0]
        self.prods = [0]
        self.state = True
        self.recent_zero = 0

    def add(self, num: int) -> None:
        self.array.append(num)
        if self.state == True:
            self.prods.append(num)
            if num != 0:
                self.state = False
            else:
                self.recent_zero = len(self.array) - 1
        elif num == 0:
            self.state = True
            self.prods.append(num)
            self.recent_zero = len(self.array) - 1
        else:
            self.prods.append(num * self.prods[-1])

    def getProduct(self, k: int) -> int:
        n = len(self.prods)
        if n - (k + 1) < self.recent_zero:
            return 0
        else:
            if self.prods[n - (k + 1)] == 0:
                return self.prods[-1]
            return self.prods[-1] // self.prods[n - (k + 1)]
