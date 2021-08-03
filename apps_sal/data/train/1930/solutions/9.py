class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self._n = n
        self._discount = discount
        self._id_to_price = {products[i]: prices[i] for i in range(len(products))}
        self._customer_no = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self._customer_no += 1
        num_purchases = len(product)
        bill = 0
        for i in range(num_purchases):
            product_id = product[i]
            quantity_of_product = amount[i]
            bill += self._id_to_price[product_id] * quantity_of_product

        if self._customer_no == self._n:
            self._customer_no = 0
            return bill - (self._discount * bill) / 100
        else:
            return bill


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
