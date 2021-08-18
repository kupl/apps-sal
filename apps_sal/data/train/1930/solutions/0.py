class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):

        self.n = n
        self.count = 0
        self.discount = discount
        self.products = {}

        for i in range(0, len(products)):

            self.products[products[i]] = prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:

        self.count += 1

        subtotal = 0

        for i in range(0, len(product)):

            subtotal += self.products[product[i]] * amount[i]

        if self.count == self.n:

            subtotal = subtotal - (self.discount * subtotal) / 100
            self.count = 0

        return subtotal
