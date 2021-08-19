class ProductOfNumbers:

    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        if num == 0:
            self.data = []
        self.data.append(num)

    def getProduct(self, k: int) -> int:
        count = 0
        if k > len(self.data):
            return 0
        res = self.data[-k:]
        return math.prod(res)
