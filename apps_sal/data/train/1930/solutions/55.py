class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.d = discount
        self.count = 0
        self.p = {}
        for i in range(len(products)):
            if products[i] not in self.p:
                self.p[products[i]] = prices[i]
            else:
                self.p[products[i]] += prices[i]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        self.count += 1
        for i in range(len(product)):
            bill += self.p[product[i]] * amount[i]
        if self.count != 0 and self.count % self.n == 0:
            bill = bill - (self.d * bill) / 100
        return bill
