class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.tofill = []

    def push(self, val: int) -> None:
        while self.tofill and self.tofill[0] < len(self.stacks) and len(self.stacks[self.tofill[0]]) == self.capacity:
            heapq.heappop(self.tofill)

        if not self.tofill:
            heapq.heappush(self.tofill, len(self.stacks))

        if self.tofill[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.tofill[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()

        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.tofill, index)
            return self.stacks[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
