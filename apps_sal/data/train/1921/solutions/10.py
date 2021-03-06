class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.availIndexes = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        while self.availIndexes and self.availIndexes[0] < len(self.stacks) and (len(self.stacks[self.availIndexes[0]]) == self.capacity):
            heappop(self.availIndexes)
        if not self.availIndexes:
            heappush(self.availIndexes, len(self.stacks))
        if self.availIndexes[0] == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.availIndexes[0]].append(val)

    def pop(self) -> int:
        while self.stacks and (not self.stacks[-1]):
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.availIndexes, index)
            return self.stacks[index].pop()
        return -1
