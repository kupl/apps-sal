class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.prod = {}
        for i in range(0, len(products)):
            self.prod[products[i]] = prices[i]
        self.idx = n
        self.dis = 1 - discount / 100
        self.cur_idx = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cur_idx += 1
        s = 0
        for i in range(0, len(product)):
            s += self.prod[product[i]] * amount[i]
        if self.cur_idx % self.idx == 0:
            s *= self.dis
        return s
