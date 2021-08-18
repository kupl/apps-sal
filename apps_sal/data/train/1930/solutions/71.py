class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices

        self.counter = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:

        self.counter += 1
        ans = 0

        for i in range(len(product)):
            ans += self.prices[self.products.index(product[i])] * amount[i]

        if self.counter == self.n:
            self.counter = 0
            ans = ans - self.discount * ans / 100.0

        return ans
