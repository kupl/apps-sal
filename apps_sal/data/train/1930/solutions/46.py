class Cashier:

    def __init__(self, n: int, discount: int, products, prices):
        self.prices_dict = dict()
        for (p, m) in zip(products, prices):
            self.prices_dict[p] = m
        self.discount = discount
        self.counts = 0
        self.n = n

    def getBill(self, product, amount) -> float:
        self.counts += 1
        money = sum((self.prices_dict[p] * a for (p, a) in zip(product, amount)))
        if self.counts % self.n == 0:
            money = money * (1 - self.discount / 100)
        return money
