class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.di = dict()
        for (i, j) in zip(products, prices):
            self.di[i] = j
        self.present = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.present += 1
        if self.present == self.n:
            tot = 0
            for (pro, amt) in zip(product, amount):
                tot += self.di[pro] * amt
            tot -= self.discount * tot / 100
            self.present = 0
            return tot
        else:
            tot = 0
            for (pro, amt) in zip(product, amount):
                tot += self.di[pro] * amt
            return tot
