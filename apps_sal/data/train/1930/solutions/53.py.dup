class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n, self.i, self.d = n, 0, discount
        self.price = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.i += 1
        s = sum(self.price[p] * a for p, a in zip(product, amount))
        return s if self.i % self.n else s * (1 - self.d / 100)
