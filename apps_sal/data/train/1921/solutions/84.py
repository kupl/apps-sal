import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = []
        self.stacks = []

    def push(self, val: int) -> None:
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.capacity:
            heapq.heappop(self.q)

        if not self.q:
            heapq.heappush(self.q, len(self.stacks))

        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index)
            return self.stacks[index].pop()

        return -1
