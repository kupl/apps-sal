class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):

        self.productsTable = {}
        for i in range(len(products)):
            self.productsTable[products[i]] = prices[i]
        self.count = 0
        self.n = n
        self.discount = discount

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = 0
        self.count += 1
        for i in range(len(product)):
            bill += self.productsTable[product[i]] * amount[i]

        if self.count == self.n:

            self.count = 0
            return bill - ((self.discount * bill) / 100)
        return bill
