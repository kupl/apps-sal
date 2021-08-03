from collections import deque


class StockSpanner:

    def __init__(self):
        # self.running_count = 0
        self.stack = deque()

    def next(self, price: int) -> int:

        weight = 1

        while self.stack and self.stack[-1][0] <= price:
            weight += self.stack.pop()[1]

        self.stack.append((price, weight))

        return weight


#         self.running_count += 1

#         if not self.queue:
#             self.queue.append((price, self.running_count))
#             return self.running_count

#         if price < self.queue[-1][0]:
#             self.queue.append((price, self.running_count))
#             return 1

#         else:
#             while self.queue and price >= self.queue[-1][0]:
#                 self.queue.pop()

#             if not self.queue:
#                 self.queue.append((price, self.running_count))
#                 return self.running_count

#             ans = self.running_count - self.queue[-1][1]
#             self.queue.append((price, self.running_count))

#             return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
