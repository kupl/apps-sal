class StockSpanner:
    # Description
    # - Collect daily price quotes for some stock
    # - Return the span of that stock's price for the 
    #   current day
    #   - max number of consecutive days (starting from
    #     today and going backwards) for which the price of
    #     the stock was less than or equal to today's price
    # [1,2,3,3,3,4] => span = [1,2,3,4,5,6]
    # 
    # conditions
    # - Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5
    # - calls <= 10000 to StockSpanner.next per test
    # - calls <= 150000 to StockSpanner.next across all test cases
    #
    # Approach

    def __init__(self):
        self.history = []
        self.output = []

    def next(self, price: int) -> int:
        less_than_count = 1
        while self.history and self.history[-1][0] <= price:
            less_than_count += self.history.pop()[1]
        self.output.append(less_than_count)
        self.history.append((price, less_than_count))
        return self.output[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

