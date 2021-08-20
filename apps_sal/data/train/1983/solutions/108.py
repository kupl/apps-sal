class ProductOfNumbers:

    def __init__(self):
        self.ll = []
        self.dd = [1]
        self.count = [0]

    def add(self, num: int) -> None:
        self.ll.append(num)
        val = self.dd[-1] * num
        if val == 0:
            temp = self.count[-1]
            self.count.append(temp + 1)
            val = self.dd[-1]
            self.dd.append(val)
        else:
            self.dd.append(val)
            temp = self.count[-1]
            self.count.append(temp)

    def getProduct(self, k: int) -> int:
        upp = len(self.count) - 1
        low = upp - k + 1
        if low == 1:
            if self.count[upp] == 0:
                return self.dd[upp]
            else:
                return 0
        elif self.count[upp] - self.count[low - 1] == 0:
            return self.dd[upp] // self.dd[low - 1]
        else:
            return 0
