from collections import defaultdict
from heapq import heappush, heappop


class DinnerPlates:

    def __init__(self, capacity: int):
        self.size = capacity
        self.stacks = []
        self.left_available = []

    def push(self, val: int) -> None:
        while self.left_available and self.left_available[0] < len(self.stacks) and len(self.stacks[self.left_available[0]]) == self.size:
            heappop(self.left_available)

        if not self.left_available:
            heappush(self.left_available, len(self.stacks))

        if self.left_available[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.left_available[0]].append(val)

    def pop(self) -> int:

        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:

            heappush(self.left_available, index)
            return self.stacks[index].pop()

        return -1
