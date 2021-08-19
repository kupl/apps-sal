class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        # self.products = products
        # self.prices = prices
        self.product_prices = dict(list(zip(products, prices)))
        self.current = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.current += 1
        bill = 0
        for i in range(len(amount)):
            bill += amount[i] * self.product_prices[product[i]]
        if self.current % self.n == 0:
            bill = (bill - bill * (self.discount / 100))
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
