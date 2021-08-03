class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.stacks = []
        self.pq = []

    def push(self, val: int) -> None:

        while self.pq and len(self.stacks) > self.pq[0] and len(self.stacks[self.pq[0]]) == self.cap:
            heapq.heappop(self.pq)
        if not self.pq:
            heapq.heappush(self.pq, len(self.stacks))
        if self.pq[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.pq[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        heapq.heappush(self.pq, index)
        return val


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
