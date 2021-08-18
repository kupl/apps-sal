class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.count = 0
        self.discount = discount

        self.prices = {prod: price for prod, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        for p, a in zip(product, amount):
            bill += (self.prices[p] * a)

        self.count += 1
        if self.count % self.n == 0:
            bill *= (1 - (self.discount / 100.))
        return bill
