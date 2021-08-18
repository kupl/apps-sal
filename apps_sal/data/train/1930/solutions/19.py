class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self._counter = 0
        self._n = n
        self._discount = discount

        self._products: Dict[int, int] = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        bill = sum([self._products[pid] * amt for pid, amt in zip(product, amount)])

        self._counter += 1
        if self._counter % self._n == 0:
            bill -= self._discount * bill / 100
            self._counter = 0

        return bill
