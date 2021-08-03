class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = {product: price for product, price in zip(products, prices)}
        self.customer_number = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        total = sum(self.prices[product[i]] * amount[i] for i in range(len(product)))
        if self.customer_number % self.n == 0:
            total *= (1 - self.discount / 100)
        self.customer_number += 1
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
