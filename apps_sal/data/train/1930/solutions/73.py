class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customer_num = 1 % n
        self.n = n
        self.discount = discount
        self.prices_by_id = {product_id: prices[idx] for idx, product_id in enumerate(products)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        if self.customer_num == 0:
            multiplier = 1 - (self.discount / 100)
        else:
            multiplier = 1
        self.customer_num = (self.customer_num + 1) % self.n
        return sum([self.prices_by_id[product[i]] * amount[i] for i in range(len(product))]) * multiplier
