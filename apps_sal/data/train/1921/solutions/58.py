class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = [[]]
        self.capacity = capacity
        self.current = 0

    def push(self, val: int) -> None:
        if len(self.stacks) <= self.current:
            self.stacks.append([])
        self.stacks[self.current].append(val)
        i = self.current
        while len(self.stacks) > i and len(self.stacks[i]) == self.capacity:
            i += 1
        if len(self.stacks) == i:
            self.stacks.append([])
        self.current = i

    def pop(self) -> int:
        l = len(self.stacks) - 1
        while l >= 0 and (not self.stacks[l]):
            self.stacks.pop()
            l -= 1
        if l == -1:
            self.current = 0
            self.stacks = [[]]
            return -1
        else:
            return self.stacks[l].pop()

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        if not self.stacks[index]:
            return -1
        else:
            v = self.stacks[index].pop()
            if index < self.current:
                self.current = index
            return v
