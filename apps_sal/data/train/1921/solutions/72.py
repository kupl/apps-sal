import heapq


class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        self.toPush = []

    def push(self, val: int) -> None:
        if not self.stacks:
            self.stacks.append([val])
        elif self.toPush and self.toPush[0] < len(self.stacks):
            i = heapq.heappop(self.toPush)
            self.stacks[i].append(val)
        else:
            self.stacks[-1].append(val)
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        if not self.stacks:
            return -1
        return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.toPush, index)
            return self.stacks[index].pop()
        return -1
