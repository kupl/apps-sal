class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.id_price_map = {}
        for i, product_id in enumerate(products):
            self.id_price_map[product_id] = prices[i]
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1

        total_price = 0
        for i, product_id in enumerate(product):
            total_price += self.id_price_map[product_id] * amount[i]

        if self.customer_count % self.n == 0:
            total_price -= (self.discount * total_price) / 100

        return total_price


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
