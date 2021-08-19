class ProductOfNumbers:

    def __init__(self):
        self.list = []
        self.mul_list = []
        self.n = -1

    def add(self, num: int) -> None:
        self.list.append(num)
        self.n += 1
        if self.mul_list:
            self.mul_list.append(self.mul_list[-1] * num)
        else:
            self.mul_list.append(num)
        if num == 0:
            self.mul_list = []

    def getProduct(self, k: int) -> int:
        if len(self.mul_list) == k:
            return self.mul_list[-1]
        elif len(self.mul_list) >= k + 1:
            return self.mul_list[-1] // self.mul_list[-(k + 1)]
        else:
            return 0
