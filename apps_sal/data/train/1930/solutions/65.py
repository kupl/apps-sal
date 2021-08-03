class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customers = 0
        self.n = n
        # self.prod=products
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


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
