class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.s = []
        self.q = []

    def push(self, val: int) -> None:
        if not self.q or self.q[0] > len(self.s) - 1:
            self.s.append([val])
            self.q = []
            if self.c > 1:
                heapq.heappush(self.q, len(self.s) - 1)
        else:
            temp = heapq.heappop(self.q)
            self.s[temp].append(val)
            if len(self.s[temp]) < self.c:
                heapq.heappush(self.q, temp)

    def pop(self) -> int:
        while self.s and not self.s[-1]:
            self.s.pop()

        if not self.s:
            return -1

        if len(self.s[-1]) == self.c:
            heapq.heappush(self.q, len(self.s) - 1)
        return self.s[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index < 0 or index > len(self.s) - 1:
            return -1

        if len(self.s[index]) == self.c:
            heapq.heappush(self.q, index)

        return self.s[index].pop() if self.s[index] else -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
