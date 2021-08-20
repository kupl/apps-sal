class ProductOfNumbers:

    def __init__(self):
        self.last_zero = -1
        self.product_agg = []

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = len(self.product_agg)
            self.product_agg.append(num)
        elif self.last_zero == len(self.product_agg) - 1:
            self.product_agg.append(num)
        else:
            self.product_agg.append(num * self.product_agg[len(self.product_agg) - 1])

    def getProduct(self, k: int) -> int:
        diff_num = len(self.product_agg) - k - 1
        if self.last_zero != -1 and self.last_zero > diff_num:
            return 0
        if diff_num >= 0 and self.product_agg[diff_num] > 0:
            return self.product_agg[len(self.product_agg) - 1] // self.product_agg[diff_num]
        return self.product_agg[len(self.product_agg) - 1]
