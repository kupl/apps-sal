class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):

        self.n = self.m = n
        self.discount = discount
        self.prices = {pro: pri for pro, pri in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:

        self.n -= 1
        res = sum(self.prices[pr] * am for pr, am in zip(product, amount))
        if not self.n:
            self.n = self.m
            return res - res * (self.discount / 100)
        return res
