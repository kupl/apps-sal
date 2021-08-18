class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.suffixProduct = []
        self.zeros = set()

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.zeros.add(len(self.nums) - 1)
            num = 1
        if len(self.suffixProduct) > 0:
            self.suffixProduct.append(self.suffixProduct[-1] * num)
        else:
            self.suffixProduct.append(num)

    def getProduct(self, k: int) -> int:
        if k == 1:
            return self.nums[-1]
        l = len(self.suffixProduct) - 1
        for zi in self.zeros:
            if zi > l - k and zi <= l:
                return 0
        if len(self.suffixProduct) == -1 * (-k):
            dd = 1
        else:
            dd = self.suffixProduct[-1 - k]
        return int(self.suffixProduct[-1] / dd)
