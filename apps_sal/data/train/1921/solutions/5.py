class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.current = 0
        self.capacity = capacity
        self.tail = 0

    def push(self, val: int) -> None:
        while self.current < len(self.stacks) and len(self.stacks[self.current]) == self.capacity:
            self.current += 1
        if self.current == len(self.stacks):
            self.stacks.append([])
        self.stacks[self.current].append(val)

    def pop(self) -> int:
        rightmost = len(self.stacks) - 1

        while rightmost >= 0 and not self.stacks[rightmost]:
            rightmost -= 1
        if rightmost == -1:
            return -1
        elem = self.stacks[rightmost][-1]
        self.stacks[rightmost].pop()
        while rightmost >= 0 and not self.stacks[rightmost]:
            self.stacks.pop()
            rightmost -= 1
        return elem

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        elem = self.stacks[index][-1]
        self.stacks[index].pop()
        if self.current > index:
            self.current = index
        return elem

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
