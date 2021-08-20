class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.p = dict()
        for (p1, p2) in zip(products, prices):
            self.p[p1] = p2
        self.d = discount
        self.n = n
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        bill = 0
        for (p, a) in zip(product, amount):
            bill += self.p[p] * a
        if self.count == self.n:
            bill -= bill * self.d / 100
            self.count = 0
        return bill
