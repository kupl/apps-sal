class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.i = 1
        self.n = n
        self.discount = discount
        self.prices = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        x = sum([self.prices[product[i]] * amount[i] for i in range(len(product))])

        if self.i == self.n:
            x = x - (self.discount * x) / 100.0
            self.i = 0
        self.i += 1
        return x


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
