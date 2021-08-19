class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity
        self.stacks = []
        self.h = []

    def push(self, val: int) -> None:
        while self.h and self.h[0] < len(self.stacks) and (len(self.stacks[self.h[0]]) == self.c):
            heapq.heappop(self.h)
        if not self.h:
            heapq.heappush(self.h, len(self.stacks))
        if self.h[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.h[0]].append(val)

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.h, index)
            return self.stacks[index].pop()
        return -1
