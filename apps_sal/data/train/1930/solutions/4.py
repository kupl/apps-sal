class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.c = 0
        self.n = n
        self.discount = discount
        self.prod_price = {prod: price for prod, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        cost = 0
        for p, a in zip(product, amount):
            cost += self.prod_price[p] * a
        self.c += 1
        if self.c == self.n:
            cost -= (cost * self.discount) / 100
            self.c = 0
        return cost
