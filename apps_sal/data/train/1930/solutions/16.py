class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.n = n
        self.prices = {key: prices[idx] for idx, key in enumerate(products)}
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        res = sum([amount[i] * self.prices[k] for i, k in enumerate(product)])
        if self.count == self.n:
            res *= (1 - self.discount / 100)
            self.count = 0
        return res


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
