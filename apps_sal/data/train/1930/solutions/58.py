class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.n_customer = 0
        self.discount = discount
        self.products = products
        self.prices = prices

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.n_customer += 1
        bill = 0
        for i in range(len(product)):
            p = product[i]
            product_index = self.products.index(p)
            bill += amount[i] * self.prices[product_index]
        if self.n_customer % self.n == 0:
            return bill - bill * self.discount / 100
        return bill
