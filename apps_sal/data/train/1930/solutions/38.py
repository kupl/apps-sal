class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.temp = n
        self.discount = 1 - (discount / 100)
        self.prices = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.n -= 1
        total = sum(self.prices[product_id] * quantity for product_id, quantity in zip(product, amount))
        if self.n == 0:
            total *= self.discount
            self.n = self.temp
        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
