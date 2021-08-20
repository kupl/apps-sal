class ProductOfNumbers:

    def __init__(self):
        self.lis = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.lis = [1]
        else:
            self.lis.append(self.lis[len(self.lis) - 1] * num)

    def getProduct(self, k: int) -> int:
        s = len(self.lis)
        if s - k - 1 < 0:
            return 0
        return int(self.lis[s - 1] / self.lis[s - k - 1])
