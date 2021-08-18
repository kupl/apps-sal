class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.discount = discount / 100
        self.n = n
        self.memo = dict()
        for a, b in zip(products, prices):
            self.memo[a] = b
        self.idx = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.idx += 1
        res = 0
        for a, b in zip(product, amount):
            res += self.memo[a] * b
        if self.idx % self.n == 0:
            res *= (1 - self.discount)
        return res
