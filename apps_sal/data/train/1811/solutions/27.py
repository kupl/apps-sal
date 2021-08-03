class StockSpanner:
    # start from back
    # from collections import deque
    # queue=deque()

    def __init__(self):
        # self.queue=deque()
        self.stack = []
    # if for the prev number is less than price we can just add one to its span, if its preceding bigger price is bigger than curr price

    def next(self, price: int) -> int:
        # span=1
        # stoppage_price=-1
        # for p,stop_price,s in self.queue:
        #     if p<=price and stop_price>price:
        #         span=s+span
        #         break
        #     elif p<=price and stop_price<=price:
        #         span+=1
        #     else:
        #         stoppage_price=p
        #         break
        # self.queue.appendleft((price,stoppage_price,span))
        # return span
        # add to stack
        # same as above sol but pop off same elements so the worst case is avoided
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
