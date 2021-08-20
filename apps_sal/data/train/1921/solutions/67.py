class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        self.pq = []

    def push(self, val: int) -> None:
        while self.pq and self.pq[0] < len(self.stacks) and (len(self.stacks[self.pq[0]]) == self.capacity):
            heapq.heappop(self.pq)
        if not self.pq:
            heapq.heappush(self.pq, len(self.stacks))
        if self.pq[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.pq[0]].append(val)

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index <= len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.pq, index)
            return self.stacks[index].pop()
        return -1
