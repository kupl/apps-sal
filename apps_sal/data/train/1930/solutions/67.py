# 749

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = dict(list(zip(products, prices)))
        self.pos = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.pos += 1
        sz = len(product)
        cost = sum([self.prices[product[i]] * amount[i] for i in range(sz)])
        if self.pos % self.n == 0:
            # discount
            cost = cost - (self.discount * cost) / 100
        return cost


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
