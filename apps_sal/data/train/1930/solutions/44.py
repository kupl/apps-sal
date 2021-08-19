class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.counter = 1

    def getBill(self, product: List[int], amounts: List[int]) -> float:
        bill = 0
        for i, product_id in enumerate(product):
            bill += amounts[i] * self.prices[self.products.index(product_id)]
        if self.counter == self.n:
            bill -= bill * (self.discount / 100)
            self.counter = 1
        else:
            self.counter += 1
        return bill
# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
