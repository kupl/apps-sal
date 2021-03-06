class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        ans = 1
        while self.st and price >= self.st[-1][0]:
            ans += self.st.pop()[1]
        self.st.append([price, ans])
        return ans
