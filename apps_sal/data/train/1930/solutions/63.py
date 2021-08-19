class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer = 1
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = 0
        for i in range(0, len(product)):
            total += self.prices[self.products.index(product[i])] * amount[i]
        if self.customer == self.n:
            total -= self.discount * total / 100
            self.customer = 1
        else:
            self.customer += 1

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
