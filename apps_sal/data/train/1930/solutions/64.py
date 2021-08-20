class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.price = dict(list(zip(products, prices)))
        self.discount = discount
        self.n = n
        self.cnt = 0

    def _calculateBillAmount(self, product: List[int], amount: List[int]) -> float:
        bill = 0.0
        for (i, p) in enumerate(product):
            bill += self.prices[p] * amount[i]
        return bill

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cnt += 1
        total = 0.0
        for (i, p) in enumerate(product):
            total += self.price[p] * amount[i]
        return total * (1 - self.discount / 100 if self.cnt % self.n == 0 else 1)
