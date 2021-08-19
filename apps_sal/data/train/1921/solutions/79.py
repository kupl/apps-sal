class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.stack = []
        self.size = capacity
        self.left = 0
        self.right = 0

    def push(self, val: int) -> None:
        if not self.stacks:
            self.stack.append(val)
            self.stacks.append(self.stack)
            self.left = 0
        else:
            while self.left < len(self.stacks) and len(self.stacks[self.left]) == self.size:
                self.left += 1
            if self.left == len(self.stacks):
                self.stacks.append([])
                self.stacks[self.left].append(val)
            else:
                self.stacks[self.left].append(val)
            self.right = len(self.stacks) - 1

    def pop(self) -> int:
        if not self.stacks:
            return -1
        if not self.stacks[self.right]:
            while not self.stacks[self.right]:
                self.stacks.pop(self.right)
                self.right -= 1
        item = self.stacks[self.right].pop()
        if not self.stacks[self.right]:
            self.stacks.pop(self.right)
            self.right -= 1
        return item

    def popAtStack(self, index: int) -> int:
        if len(self.stacks) - 1 < index:
            return -1
        if not self.stacks[index]:
            return -1
        if self.stacks[index]:
            if self.left > index:
                self.left = index
        return self.stacks[index].pop()
