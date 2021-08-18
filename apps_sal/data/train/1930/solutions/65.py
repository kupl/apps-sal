class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customers = 0
        self.n = n
        self.prices = prices
        self.discount = discount
        self.products = {}
        for i in range(len(products)):
            self.products[products[i]] = i

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        self.customers += 1
        for i in range(len(product)):
            bill += (amount[i] * (self.prices[self.products[product[i]]]))
        if(self.customers == self.n):
            bill = bill - (bill * self.discount / 100)
            self.customers = 0
        return bill
