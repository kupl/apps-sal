class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.incre = []
        self.amount = 0

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            if self.amount:
                heapq.heappush(self.incre, (-len(self.stack), self.amount))
                self.amount = 0
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            while self.incre and len(self.stack) == -self.incre[0][0]:
                self.amount += heapq.heappop(self.incre)[1]
            return self.amount + self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        heapq.heappush(self.incre, (-min(k, len(self.stack)), val))


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

