class Cashier:
    from functools import lru_cache

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.d = discount
        self.p = products
        self.amt = prices
        self.c = 0

    @lru_cache(maxsize=128)
    def compute_amount(self, pdt, qty):
        bill = 0
        for p, q in zip(pdt, qty):
            i = self.p.index(p)
            bill += self.amt[i] * q
        return bill

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.c += 1
        amt = self.compute_amount(tuple(product), tuple(amount))
        if self.c % self.n == 0 and self.d:
            return amt - (amt * self.d / 100)
        else:
            return amt
