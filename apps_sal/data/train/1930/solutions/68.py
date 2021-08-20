class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.ctr = 0
        self.n = n
        self.discount = (100 - discount) / 100
        self.products = dict()
        for idx in range(len(products)):
            self.products[products[idx]] = prices[idx]

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.ctr += 1
        cost = 0
        for idx in range(len(product)):
            itemId = product[idx]
            cost += self.products[itemId] * amount[idx]
        if self.ctr % self.n == 0:
            self.ctr = 0
            cost = self.discount * cost
        return cost
