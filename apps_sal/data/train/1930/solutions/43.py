class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount
        self.n = n
        self.products = {product: price for product, price in zip(products, prices)}
        self.customers = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customers += 1
        bill = sum([self.products[prod] * amnt for prod, amnt in zip(product, amount)])
        if (self.customers % self.n) == 0:
            self.customers = 0
            bill -= bill * self.discount / 100
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
