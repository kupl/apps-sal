class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.product_map = { products[i]: prices[i] for i in range(len(products))}
        self.prices = prices
        self.customer_count = 0
        self.discount = discount/100
        self.discount_customer = n
        

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        bill = 0
        discount = 0
        for i in range(len(product)):
            bill += amount[i] * self.product_map[product[i]]
        if self.customer_count == self.discount_customer:
            discount = self.discount * bill
            self.customer_count = 0
            bill = bill - discount
        return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)

