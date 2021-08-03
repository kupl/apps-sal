class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount_limit = n
        self.discount_count = n
        self.discount = discount
        self.prices = prices

        self.products = {}
        i = 0
        for p in products:
            self.products[str(p)] = i
            i += 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.discount_count -= 1

        bill = 0.0
        for item in range(len(product)):
            bill += self.prices[self.products[str(product[item])]] * amount[item]

        if self.discount_count < 1:
            bill = bill - (self.discount * bill) / 100
            self.discount_count = self.discount_limit

        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
