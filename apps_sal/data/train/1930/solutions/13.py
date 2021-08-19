class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        prod_price = {}
        for i in range(len(products)):
            prod_id = products[i]
            price = prices[i]
            prod_price[prod_id] = price
        self.prod_price = prod_price
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        if self.count % self.n == 0:
            d = self.discount
        else:
            d = 0
        bill = 0
        for i in range(len(product)):
            p_id = product[i]
            a = amount[i]
            price = self.prod_price[p_id]
            bill += a * price
        return bill - bill * d / 100
